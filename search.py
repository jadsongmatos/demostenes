import duckdb
from transformers import BigBirdModel, BigBirdTokenizerFast

import argostranslate.package
import argostranslate.translate

import pandas as pd
import numpy as np

conn = duckdb.connect(database='jus.duckdb', read_only=True)

resultado = conn.execute("select data from embedding LIMIT 1;").fetchall()

print("resultado",len(resultado[0][0]))

test = conn.execute("select * from embedding where data = ?;",resultado[0]).df()
print(test.head)

test = conn.execute("""
WITH my_embedding AS (
  SELECT 0 AS id,$data AS data
  UNION ALL
  SELECT * FROM embedding             
),
my_embedding_norm AS (
  SELECT 0 AS id,$norm AS norm
  UNION ALL
  SELECT * FROM embedding_norm             
),
DotProducts AS (
    WITH expanded AS (
        WITH norm_prox AS (
          (SELECT id, norm
          FROM my_embedding_norm
          WHERE norm < $norm
          ORDER BY norm DESC
          LIMIT 128)

          UNION ALL

          (SELECT id, norm
          FROM my_embedding_norm
          WHERE norm >= $norm
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
    idA,
    idB,
    cosine_similarity
FROM 
    CosineSimilarities
WHERE 
    cosine_similarity > 0.7;
""",{
  "data": resultado[0][0],
  "norm": 42
}).df()

print(test.head)
