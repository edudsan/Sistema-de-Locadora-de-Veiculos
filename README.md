# 🚗 Sistema de Gestão de Locadora de Veículos v2.0

## 📄 1. Visão Geral do Projeto

Este projeto é uma **API RESTful robusta** para a gestão completa de uma locadora de veículos. Desenvolvido em **Python** com **FastAPI** e **Docker**, garante portabilidade e facilidade de implantação.

Permite o gerenciamento de **clientes** (pessoas físicas e jurídicas), **frota de veículos** e **reservas**, com funcionalidades como busca de veículos disponíveis e relatórios de faturamento.

Para acompanhar o andamento das atividades do projeto **Sistema de Gestão de Locadora de Veículos**, o quadro Kanban foi configurado no **Trello**.

Você pode acessar o Kanban e acompanhar as tarefas do projeto através do seguinte [link para o Kanban no Trello](https://trello.com/invite/b/686d7b801b1717d639cdf73a/ATTI0e537f72d7f7bcf00045a38796dfefed24A3213C/sistema-locadora).

O uso do Kanban auxilia na visualização do progresso, identificação de bloqueios e priorização de tarefas, além de promover uma melhor organização das sprints e entregas do projeto.

### 🔄 1.1 Evolução do Projeto

Refatoração completa de um projeto **Java** orientado a objetos para uma arquitetura **moderna e desacoplada**.

[👁️ Projeto Original (Java)](https://github.com/edudsan/Grupo-08---OO/tree/main/Trabalho_OO/src)

Principais melhorias:

* **Princípios SOLID**
* **DevOps** e conteinerização
* **Modularização** e **testes automatizados**

---

## 🛠️ 2. Arquitetura e Melhorias Técnicas

| Categoria        | Projeto Java               | Projeto Python + API               | Vantagens                             |
| ---------------- | -------------------------- | ---------------------------------- | ------------------------------------- |
| **Arquitetura**  | Monolítica Desktop (Swing) | **RESTful** + frontend desacoplado | Flexível, escalável.                  |
| **Persistência** | Em memória                 | **PostgreSQL**                     | Dados persistentes e seguros.         |
| **Estrutura**    | Pacotes acoplados          | **Módulos por domínio**            | Manutenção facilitada.                |
| **Implantação**  | JAR manual                 | **Docker & Compose**               | Ambiente reproduzível com um comando. |
| **Qualidade**    | Sem testes                 | **Pytest + Pylint**                | Confiável e com padrões de código.    |

---

## 🔧 3. Tecnologias Utilizadas

* **Backend:**

  * Python 3.11
  * FastAPI
  * Pydantic
  * Psycopg2

* **Banco de Dados:**

  * PostgreSQL 17

* **Frontend:**

  * HTML5, CSS3, JavaScript (Vanilla)

* **Testes & Qualidade:**

  * Pytest
  * HTTPX
  * Pylint

* **DevOps:**

  * Docker & Docker Compose

---

## 🗂️ 4. Estrutura do Projeto

```plaintext
.
│
│   .dockerignore           # 📄 Arquivo que define quais arquivos e pastas devem ser ignorados pelo Docker ao construir a imagem.
│   .env                    # 🔑 Arquivo de configuração para variáveis de ambiente, como senhas e nomes de banco de dados. Não deve ser enviado para o GitHub.
│   .pylintrc               # ⚙️ Arquivo de configuração para o Pylint, definindo as regras de análise estática e qualidade do código.
│   docker-compose.yml      # 🐳 Orquestrador dos containers. Define e conecta os serviços da aplicação (app, db, tests, lint).
│   Dockerfile              # 📦 Receita para construir a imagem Docker da aplicação, instalando Python, dependências e configurando o ambiente.
│   organize_tests.bat      # 🛠️ (Assumindo ser um dos scripts que criamos) Script para automatizar a reorganização da estrutura de pastas do projeto.
│   requirements.txt        # 📦 Lista de todas as dependências Python necessárias para o projeto (FastAPI, Pylint, etc.).
│   wait-for-db.sh          # ⏳ Script de shell que força a aplicação a esperar o banco de dados estar 100% pronto antes de iniciar.
│
├───database
│   └───init                # 🗄️ Scripts que o PostgreSQL executa automaticamente ao criar o banco de dados pela primeira vez.
│           01_schema.sql   #    -> Define a estrutura das tabelas (CREATE TABLE...).
│           02_data.sql     #    -> Popula o banco com dados iniciais para teste e demonstração (INSERT INTO...).
│
├───frontend                # 🖥️ Interface do Usuário. Todos os arquivos que rodam no navegador do cliente.
│       index.html          #    -> A estrutura principal da página web (o "esqueleto").
│       script.js           #    -> Contém toda a lógica e interatividade da página (faz chamadas à API, manipula a interface).
│       style.css           #    -> Define a aparência e o estilo visual da aplicação.
│
└───src                     # 📦 Pasta principal que contém todo o código-fonte da aplicação Python.
    │   main.py             #    -> Ponto de entrada da API. Inicializa o FastAPI e inclui os routers dos módulos.
    │
    ├───cliente             # 👤 Módulo autocontido para a funcionalidade de "Cliente".
    │       router.py       #    -> Define os endpoints da API para Clientes (ex: GET /clientes, POST /clientes).
    │       schema.py       #    -> Define os modelos de dados (schemas Pydantic) para Cliente e Endereço.
    │       service.py      #    -> Contém a lógica de negócio e as queries ao banco de dados para Clientes.
    │       test_cliente.py #    -> Testes de integração específicos para os endpoints do módulo Cliente.
    │       __init__.py     #    -> Torna a pasta 'cliente' um pacote Python.
    │
    ├───database
    │       connection.py   #    -> Centraliza a lógica de conexão com o banco de dados e a função de dependência do FastAPI.
    │
    ├───reserva             # 📅 Módulo autocontido para a funcionalidade de "Reserva".
    │       router.py       #    -> Define os endpoints da API para Reservas.
    │       schema.py       #    -> Define os modelos de dados (schemas Pydantic) para Reserva e Relatórios.
    │       service.py      #    -> Contém a lógica de negócio e as queries ao banco para Reservas.
    │       test_reserva.py #    -> Testes de integração específicos para os endpoints do módulo Reserva.
    │       __init__.py     #    -> Torna a pasta 'reserva' um pacote Python.
    │
    └───veiculo             # 🚗 Módulo autocontido para a funcionalidade de "Veículo".
            router.py       #    -> Define os endpoints da API para Veículos.
            schema.py       #    -> Define os modelos de dados (schemas Pydantic) para Veículo.
            service.py      #    -> Contém a lógica de negócio e as queries ao banco para Veículos.
            test_veiculo.py #    -> Testes de integração específicos para os endpoints do módulo Veículo.
            __init__.py     #    -> Torna a pasta 'veiculo' um pacote Python.
```

---

## 🔄 5. Como Executar o Projeto

**Pré-requisitos:** Docker e Docker Compose instalados na sua máquina.

### 🔋 5.1 Iniciar a Aplicação

Para iniciar a aplicação web e o banco de dados, execute o seguinte comando na raiz do projeto. Este comando também irá reconstruir as imagens se necessário.

```sh
docker-compose up --build
```

Após a inicialização, a interface web estará acessível em http://localhost:8000 e a documentação interativa da API (Swagger UI) em http://localhost:8000/docs.


### 📝 5.2 Rodar Testes Automatizados

Para executar a suíte de testes completa, que valida todos os endpoints, abra um novo terminal (deixe a aplicação rodando no primeiro) e execute:

```
docker-compose run --rm tests
```

Este comando inicia um container temporário que executa o pytest, valida todos os módulos e é removido ao final, garantindo um ambiente de teste limpo.


### 📚 5.3 Análise de Código (Pylint)

Para verificar a qualidade e o estilo do código em relação às boas práticas do Python, execute:

```
docker-compose run --rm lint
```
---


## 🧪 6. Testes Automatizados com Pytest 

Este repositório contém testes automatizados utilizando o framework `pytest`. Siga os passos abaixo para configurar o ambiente e executar os testes sem problemas.

---

## 🛠 6.1 Pré-requisitos

Antes de iniciar, verifique se você possui o Python 3.8 ou superior instalado em sua máquina. Você pode verificar a versão do Python com o comando:

```bash
python --version
```

---

### 🚀 6.2 Passo a Passo para Executar os Testes

#### 6.2.1 Crie um Ambiente Virtual

Para garantir que as dependências não afetem outras aplicações na sua máquina, crie um ambiente virtual exclusivo para os testes:

```bash
python -m venv venv_testes
```

#### 6.2.2 Ative o Ambiente Virtual

- **No Windows**:

```bash
.\venv_testes\Scripts\activate
```

- **No Linux ou MacOS**:

```bash
source venv_testes/bin/activate
```

> 🔑 **Importante:** Todos os comandos a seguir devem ser executados com o ambiente virtual ativado.

---

#### 6.2.3 Instale as Dependências Necessárias

As dependências dos testes estão listadas no arquivo `requirements-test.txt`. Instale todas elas com o comando:

```bash
pip install -r requirements-test.txt
```

---

#### 6.2.4 Atualize o Gerenciador de Pacotes (pip)

Para garantir que você está usando a versão mais recente do `pip`, execute:

```bash
python.exe -m pip install --upgrade pip
```

---

#### 6.2.5 Execute os Testes Automatizados

Com todas as dependências instaladas e o ambiente configurado, execute os testes com o comando abaixo:

```bash
pytest tests_e2e/
```

---

### 💡 6.3 Dicas Úteis

- Para ver um relatório mais detalhado dos testes, adicione a flag `-v`:
  
```bash
pytest -v tests_e2e/
```

- Para gerar um relatório em HTML (caso o plugin esteja no `requirements-test.txt`):

```bash
pytest --html=report.html tests_e2e/
```

---

### 🧹 6.4 Desativando o Ambiente Virtual

Após rodar os testes, você pode desativar o ambiente virtual com:

```bash
deactivate
```

## 🛠 7. Convenções de Código

- **Estilo**: [PEP 8](https://peps.python.org/pep-0008/)
- **Commits**: [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- **Branching**: `main` como principal, sem ramificações adicionais.

---

## Referências Técnicas

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/docs/current/)
- [pytest](https://docs.pytest.org/en/stable/)
- [Docker Compose](https://docs.docker.com/compose/)

| Autor        | Matrícula | Disciplina                                                           | Período |
|--------------|-----------|----------------------------------------------------------------------|---------|
| Eduardo Schuindt Santos | 202042927| Técnicas de Programação em Plataformas Emergentes (FGA0242) – UnB/FCTE | 2025/1  |

---