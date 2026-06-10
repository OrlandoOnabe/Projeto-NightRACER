# NightRACER - Sistema de Compra de Ingressos para Corridas

## Integrantes
- Orlando Nagrockis Bertholdo RA: 24.223.003-5
- Lorenzo Colonnese Chiganças RA: 24.223.085-2
- Paulo Gabriel Gonçalves Leme RA: 24.123.075-4
- Morgana Rodrigues Zanetti RA: 24.223.010-0

---

# 1. Tema do Projeto

O projeto NightRACER consiste em um sistema de compra e gerenciamento de ingressos para eventos automobilísticos, permitindo o cadastro de usuários, visualização de corridas, gerenciamento de carrinho de compras e registro de pedidos.

O sistema possui suporte para diferentes categorias de corridas, como:
- Fórmula 1 (F1)
- NASCAR
- MotoGP

Cada categoria pode possuir atributos específicos, aproveitando a flexibilidade dos bancos NoSQL orientados a documentos.

O sistema foi desenvolvido utilizando o conceito de **Polyglot Persistence**, no qual diferentes bancos de dados são utilizados conforme o tipo de dado e a necessidade da aplicação.

---

# 2. Arquitetura do Projeto

O projeto utiliza:

```text
Frontend CLI (Python)
        ↓
Backend (Python)
        ↓
──────────────────────────
Supabase (Relacional)
MongoDB (Document Storage)
Cassandra (Wide Column)
Redis (Key-Value)
──────────────────────────
```

---

# 3. Justificativa dos Bancos Utilizados

## 3.1 Supabase (Banco Relacional)

Utilizado para armazenar:
- usuários
- clientes
- administradores

### Justificativa

Os dados dos usuários possuem:
- estrutura fixa
- relacionamentos bem definidos
- necessidade de consistência

O modelo relacional foi escolhido por ser ideal para:
- autenticação
- integridade dos dados
- armazenamento estruturado

### CRUD Implementado

- Cadastro de usuário
- Login
- Atualização de perfil
- Exclusão de conta
- Listagem de clientes

---

## 3.2 MongoDB (Document Storage)

Utilizado para armazenar:
- corridas
- informações específicas de categorias

### Justificativa

As diferentes categorias de corrida possuem atributos variáveis.

Exemplos:
- MotoGP → cilindrada
- F1 → quantidade de voltas
- NASCAR → tipo de pista

O MongoDB foi escolhido por permitir:
- documentos flexíveis
- fácil expansão de atributos
- armazenamento sem schema rígido

### CRUD Implementado

- Cadastro de corrida
- Atualização de corrida
- Remoção de corrida
- Listagem de corridas

---

## 3.3 Cassandra (Wide Column)

Utilizado para armazenar:
- pedidos realizados
- histórico de compras

### Justificativa

Os pedidos possuem:
- grande volume potencial
- necessidade de consultas rápidas
- foco em escalabilidade

O Cassandra foi escolhido por:
- alta performance
- arquitetura distribuída
- modelo wide-column adequado para histórico de pedidos

### CRUD Implementado

- Registro de pedido
- Atualização de status de pagamento
- Histórico de compras
- Cancelamento de pedidos

---

## 3.4 Redis (Key-Value)

Utilizado para armazenar:
- carrinho de compras temporário

### Justificativa

O carrinho necessita:
- acesso extremamente rápido
- armazenamento temporário
- expiração automática opcional

O Redis foi escolhido por:
- armazenamento em memória
- alta velocidade
- modelo key-value ideal para carrinhos

### CRUD Implementado

- Adicionar item ao carrinho
- Visualizar carrinho
- Atualizar quantidade
- Remover item
- Limpar carrinho após compra

---

# 4. Tecnologias Utilizadas

## Linguagem
- Python 3

## Bancos
- Supabase
- MongoDB
- Apache Cassandra
- Redis

## Containers
- Docker

## Bibliotecas Python
- supabase
- pymongo
- cassandra-driver
- redis

---

# 5. Como Executar o Projeto

## 5.1 Requisitos

Instalar:
- Python 3
- Docker

---

## 5.2 Instalar dependências Python

O uso de ambiente virtual é recomendado para evitar conflitos entre bibliotecas Python.

### Linux

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar ambiente virtual:

```bash
source venv/bin/activate
```

---

### Windows

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar ambiente virtual:

```bash
venv\Scripts\activate
```

---

### Instalar dependências

```bash
pip install -r dependencias.txt
```

---

## 5.3 Executar Cassandra

### Criar container

```bash
docker run --name cassandra -p 9042:9042 -d cassandra
```

### Inicializar Cassandra

```bash
docker start cassandra
```

```bash
docker ps
```

### Entrar no Cassandra

```bash
docker exec -it cassandra cqlsh
```

---

## 5.4 Criar Keyspace Cassandra

```sql
CREATE KEYSPACE NightRACER
WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': 1
};
```

---

## 5.5 Selecionar Keyspace

```sql
USE NightRACER;
```

---

## 5.6 Criar tabela de pedidos

```sql
CREATE TABLE pedidos (
    id_pedido uuid,
    id_usuario int,
    id_corrida text,
    nome_corrida text,
    categoria text,
    data_pedido timestamp,
    qtd_ingressos int,
    valor_pedido decimal,
    status_pedido text,
    tipo_pagamento text,

    PRIMARY KEY (id_usuario, data_pedido)
);
```

---

## 5.7 Executar Redis

### Criar container

```bash
docker run --name redis -p 6379:6379 -d redis
```

### Inicializar Redis

```bash
docker start redis
```

```bash
docker ps
```

### Entrar no Redis

```bash
docker exec -it redis redis-cli
```

---

## 5.8 MongoDB Atlas

O projeto utiliza MongoDB Atlas em nuvem.

É necessário:
- criar cluster MongoDB Atlas
- adicionar string de conexão no arquivo `db1.py`

Exemplo:

```python
MongoClient("mongodb+srv://usuario:senha@cluster.mongodb.net/")
```

---

## 5.9 Supabase

O projeto utiliza Supabase em nuvem.

É necessário:
- criar projeto Supabase
- criar tabela `usuários`
- adicionar URL e API KEY no arquivo `rdb.py`

---

# 6. Executar Projeto

Após iniciar todos os serviços:

```bash
python projeto.py
```
> Em alguns sistemas Linux pode ser necessário utilizar `python3` no lugar de `python`.

---

# 7. Funcionalidades

## Cliente
- cadastro
- login
- visualizar corridas
- adicionar ao carrinho
- atualizar carrinho
- remover itens do carrinho
- finalizar compra
- visualizar histórico

## Administrador
- cadastrar corrida
- atualizar corrida
- cancelar corrida
- listar clientes

---
