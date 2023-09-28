Categorias:
nome

Users:
id // django
password // django
last_login // django
is_superuser // django
username // django
first_name // django
last_name // django
email // django
is_staff // django
is_active // django
date_joined // django

Location:
id,
address,
latitude,
longitude,
city,
state,
nation,
user_id

Contatos:
id,
id_user,
tipo_contato,
valor,

Pedidos://Sales_facts
id,
id_produto,
id_cliente,
create_time,
update_time,
status,

Itens_pedido:
id,
id_pedido,
id_produto,
quantidade,
preco_unit,
desconto,
taxa,

Produtos:
id,
nome,
descricao,
status,
tempo_duracao,
preco_unit
stock,
id_categoria,
id_fornecedor,

Fatura:
id,
id_pedido
id_produto
id_cliente
data
desconto
notas
status
preco_unit
termos_pagamentos

Pagamentos:
id,
id_pedido,
?id_membro,
?id_projeto,
?id_cliente,
notas,
data,
valor,
meio_pagamento,

Transacoes:
id,
data,
descricao
quantidade,
taxavel,
id_conta
id_pagamento
data_venda_compra
preco_venda_compra
quantia_deposito
numero_unidades
custo_servico
juros_ganhos
numero_referencia
quantia_retirada

Gastos:
id,
valor
tipo,
valor_adiantado
data_compra
finalidade
meio_pagamento

Sales_facts