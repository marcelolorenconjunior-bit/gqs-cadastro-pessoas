# Guia de Contribuicao

Este documento define os padroes adotados no desenvolvimento e evolucao do projeto **Cadastro de Pessoas**.

## 1. Preparacao do Ambiente
- Crie um ambiente virtual (.venv) e instale as dependencias via equirements.txt.
- Ative os hooks locais antes de realizar commits:
  `powershell
  python -m pre_commit install
  `

## 2. Padroes de Codigo e Qualidade
- Siga a separacao de camadas: interface CLI em src/main.py, regras em src/cadastro.py, modelo em src/pessoa.py e persistencia nos repositorios.
- Todo codigo Python deve passar sem erros pelo **Pylint** (.pylintrc) e manter baixa complexidade ciclomatica (**Radon**).
- Nenhum commit sera aceito se falhar nos hooks do **pre-commit** (pylint e pytest).

## 3. Convencao de Commits
Utilize prefixos semanticos claros para identificar o proposito de cada alteracao:
- eat: nova funcionalidade
- ix: correcao de defeito
- efactor: melhoria estrutural sem alterar comportamento
- 	est: adicao ou ajuste de testes automatizados
- docs: atualizacao de documentacao
- chore: configuracoes de ferramentas e infraestrutura

## 4. Fluxo de Branches e Pull Requests
1. Faca um **Fork** do repositorio (para colaboradores externos) ou crie uma **branch** descritiva a partir da main (ex: eat/nova-funcionalidade, ix/corrige-busca).
2. Implemente as alteracoes e escreva ou atualize os testes em 	ests/.
3. Execute python -m pre_commit run --all-files para validar qualidade e testes antes da integracao.
4. Envie a branch para o GitHub e abra um **Pull Request** descrevendo o problema resolvido e como testar.
5. Aguarde a revisao de codigo antes de realizar o merge na main.
