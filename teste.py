import pandas as pd

carros_csv = 'db_data/carros.csv'
clientes_csv = 'db_data/clientes.csv'
funcionarios_csv = 'db_data/funcionarios.csv'
vendas_csv = 'db_data/vendas.csv'

carros_df = pd.read_csv(carros_csv)
carros_df.rename(columns={"id": "carro_id"},inplace=True)
clientes_df = pd.read_csv(clientes_csv)
clientes_df.rename(columns={"id": "cliente_id"},inplace=True)
funcionarios_df = pd.read_csv(funcionarios_csv)
funcionarios_df.rename(columns={"id": "funcionario_id"},inplace=True)
vendas_df = pd.read_csv(vendas_csv)
vendas_carros_df = vendas_df.merge(carros_df, on='carro_id', suffixes=('', '_carro'))


vendas_carros_clientes_df = vendas_carros_df.merge(clientes_df, on='cliente_id', suffixes=('', '_cliente'))

final_df = vendas_carros_clientes_df.merge(funcionarios_df, on='funcionario_id', suffixes=('', '_funcionario'))


final_df = final_df[['id', 'data_da_venda',
       'preco_de_venda', 'marca', 'modelo', 'ano', 'preco_de_lista', 'nome',
       'endereco', 'telefone', 'nome_funcionario', 'cargo', 'salario']]


for i in range(1, 7):
    final_df[f'enredeco_{i}'] = final_df['endereco']

compressions = [
    'snappy',
    'gzip',
    'brotli',
    'zstd',
    'lz4',
    'none'
]

for compression in compressions:
    final_df.to_parquet(F'db_data/sales_data_{compression}.parquet', engine='pyarrow', compression=compression)
