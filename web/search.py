import duckdb
from transformers import BigBirdModel, BigBirdTokenizerFast

import argostranslate.package
import argostranslate.translate

import numpy as np

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == "pt" and x.to_code == "en", available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())


tokenizer = BigBirdTokenizerFast.from_pretrained(
    "google/bigbird-roberta-base")  # large
model = BigBirdModel.from_pretrained("google/bigbird-roberta-base",
                                    attention_type="original_full"
                                    #attention_type="block_sparse"
                                    )

conn = duckdb.connect(database='jus.duckdb', read_only=True)

def summarizer(id):
    with open("./web/static/proc/"+str(id)+".txt", 'r') as arquivo:
        content = arquivo.readline()
        content = content+arquivo.readline()
        content = content+arquivo.readline()
        return content

def search_db(content):

    translatedText = argostranslate.translate.translate(content, "pt", "en")

    inputs = tokenizer(translatedText, return_tensors="pt")
    outputs = model(**inputs)

    vetor = outputs.last_hidden_state[0].flatten().detach().numpy() #.astype(np.float16)

    norma = float(np.linalg.norm(vetor))

    docs = conn.execute("""
    WITH my_embedding AS (
    SELECT 0 AS id,$data AS data
    UNION ALL
    SELECT * FROM embedding             
    ),
    my_embedding_norm AS (
    SELECT 0 AS id,$norma AS norm
    UNION ALL
    SELECT * FROM embedding_norm             
    ),
    DotProducts AS (
        WITH expanded AS (
            WITH norm_prox AS (
            (SELECT id, norm
            FROM my_embedding_norm
            WHERE norm < $norma
            ORDER BY norm DESC
            LIMIT 128)

            UNION ALL

            (SELECT id, norm
            FROM my_embedding_norm
            WHERE norm >= $norma
            ORDER BY norm ASC
            LIMIT 128)
            )
            SELECT
                a.id AS idA,
                b.id AS idB,
                unnest(a_data.data) AS a_data,
                unnest(b_data.data) AS b_data
            FROM
                norm_prox a
            INNER JOIN
                norm_prox b ON a.id < b.id
            JOIN my_embedding a_data ON a.id = a_data.id
            JOIN my_embedding b_data ON b.id = b_data.id
        )
        SELECT
            idA,
            idB,
            sum(a_data * b_data) AS dot_product
        FROM
            expanded
        GROUP BY
            idA, idB
    ),
    CosineSimilarities AS (
        SELECT 
            d.idA,
            d.idB,
            CASE 
                WHEN n1.norm = 0 OR n2.norm = 0 THEN 0
                ELSE d.dot_product / (n1.norm * n2.norm)
            END AS cosine_similarity            
        FROM 
            DotProducts d
        JOIN 
            my_embedding_norm n1 ON d.idA = n1.id
        JOIN 
            my_embedding_norm n2 ON d.idB = n2.id
        WHERE 
            d.idA < d.idB
    )
    SELECT 
        idB,
        cosine_similarity
    FROM 
        CosineSimilarities
    WHERE 
        cosine_similarity > 0.2 and idA = 0
    ORDER BY 
        cosine_similarity DESC;
    """,{
        "data": vetor,
        "norma": norma
    }).df()

    docs['cosine_similarity'] = docs['cosine_similarity'].round(2)
    docs['summarizer'] = docs['idB'].apply(lambda x: summarizer(x))

    return docs.to_numpy().tolist()