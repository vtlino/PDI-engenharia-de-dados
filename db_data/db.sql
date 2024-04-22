DROP DATABASE IF EXISTS loja_carros;
CREATE DATABASE loja_carros;

\c loja_carros;


CREATE TABLE carros (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(100),
    modelo VARCHAR(100),
    ano INT,
    preco_de_lista NUMERIC(10, 2)
);

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(255),
    telefone VARCHAR(15)
);

CREATE TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(50),
    salario NUMERIC(10, 2)
);

CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    carro_id INT,
    cliente_id INT,
    funcionario_id INT,
    data_da_venda DATE,
    preco_de_venda NUMERIC(10, 2),
    FOREIGN KEY (carro_id) REFERENCES carros (id),
    FOREIGN KEY (cliente_id) REFERENCES clientes (id),
    FOREIGN KEY (funcionario_id) REFERENCES funcionarios (id)
);


\copy carros FROM '/docker-entrypoint-initdb.d/carros.csv' DELIMITER ',' CSV HEADER;
\copy clientes FROM '/docker-entrypoint-initdb.d/clientes.csv' DELIMITER ',' CSV HEADER;
\copy funcionarios FROM '/docker-entrypoint-initdb.d/funcionarios.csv' DELIMITER ',' CSV HEADER;
\copy vendas FROM '/docker-entrypoint-initdb.d/vendas.csv' DELIMITER ',' CSV HEADER;
