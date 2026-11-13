# Sistema de Cadastro de Pessoas

Projeto Integrador da disciplina de **Gestao da Qualidade de Software** (UTFPR), demonstrando a evolucao progressiva de um sistema de Cadastro de Pessoas com aplicacao integrada de boas praticas de engenharia e qualidade de software.

## Funcionalidades
- **Cadastrar pessoa:** registra nome, idade e e-mail.
- **Consultar pessoa:** busca uma pessoa cadastrada pelo nome.
- **Alterar pessoa:** atualiza nome, idade e e-mail de um registro existente.
- **Listar pessoas:** exibe todas as pessoas cadastradas e o total.

## Estrutura do Repositorio
`	ext
gqs-cadastro-pessoas/
├── src/
│   ├── pessoa.py                       # Entidade Pessoa (encapsulamento e getters/setters)
│   ├── cadastro.py                     # Regras de negocio e delegacao ao repositorio
│   ├── repositorio_pessoas.py          # Contrato abstrato de persistencia (ABC)
│   ├── repositorio_pessoas_memoria.py  # Implementacao em memoria
│   ├── repositorio_pessoas_mysql.py    # Implementacao DAO com MySQL
│   └── main.py                         # Interface CLI e selecao do repositorio
├── tests/
│   └── test_cadastro.py                # Testes automatizados com PyTest
├── infra/
│   ├── compose.yaml                    # Servicos MySQL 8.4.13 (principal e replica)
│   └── init.sql                        # Script de criacao do banco e tabela pessoa
├── .gitignore                          # Arquivos e pastas ignorados pelo Git
├── .pre-commit-config.yaml             # Hooks automatizados (Pylint e PyTest)
├── .pylintrc                           # Configuracao de analise estatica
├── pytest.ini                          # Configuracao de execucao do PyTest
├── requirements.txt                    # Dependencias Python do projeto
├── README.md                           # Documentacao principal
└── CONTRIBUTING.md                     # Guia de contribuicao e padroes
`

## Tecnologias e Ferramentas
- **Linguagem:** Python 3
- **Banco de Dados e Infraestrutura:** MySQL 8.4.13, Docker e Docker Compose
- **Qualidade e Testes:** Pylint, Radon, PyTest e pre-commit
- **Versionamento:** Git e GitHub

## Como Preparar o Ambiente
1. Clone o repositorio e acesse a pasta:
   `powershell
   git clone https://github.com
   cd gqs-cadastro-pessoas
   `
2. Crie e ative o ambiente virtual:
   `powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   `
3. Instale as dependencias e os hooks do pre-commit:
   `powershell
   python -m pip install -r requirements.txt
   python -m pre_commit install
   `

## Como Executar o Sistema
- **Modo em memoria (padrao):**
  `powershell
  python src/main.py
  `
- **Modo com persistencia MySQL (Docker):**
  1. Suba os conteineres MySQL:
     `powershell
     docker compose -f infra/compose.yaml up -d
     `
  2. Crie a tabela inicial no MySQL principal:
     `powershell
     Get-Content infra/init.sql | docker exec -i mysql-principal mysql -uroot -proot
     `
  3. Defina as variaveis de ambiente e execute:
     `powershell
     \="true"
     python src/main.py
     `

## Como Executar Testes e Analise de Qualidade
- **Testes automatizados (PyTest):**
  `powershell
  python -m pytest -v
  `
- **Analise estatica (Pylint) e Complexidade (Radon):**
  `powershell
  python -m pylint src tests
  python -m radon cc src -a -s
  `

## Praticas de Qualidade Incorporadas
- Modularizacao e separacao de responsabilidades com Orientacao a Objetos e padrao Repositorio (DAO).
- Medicao de complexidade ciclomatica com Radon e padronizacao com Pylint.
- Bloqueio preventivo de defeitos via hooks do pre-commit executando Pylint e PyTest antes de cada commit.
- Persistencia relacional isolada em conteineres Docker com suporte a replicacao GTID.
