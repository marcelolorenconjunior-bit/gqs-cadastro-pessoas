# Diretrizes de Contribuição - Cadastro de Pessoas

Este projeto adota padrões explícitos para garantir a qualidade de produto e manutenibilidade do código.

## 1. Convenções de Código
* Seguir as recomendações gerais da PEP 8 para a linguagem Python.
* Todas as funções devem conter `docstrings` explicativas em formato de string tripla.
* Variáveis e funções devem utilizar nomenclatura em padrão `snake_case`.

## 2. Utilização do PyLint
* Antes de submeter qualquer alteração, execute a análise estática localmente:
  ```bash
  python -m pylint cadastro.py
  ```
* O código deve buscar aderência às regras configuradas no arquivo `.pylintrc`.

## 3. Organização de Commits
* Adotamos o padrão de commits semânticos simplificado:
  * `chore:` para alterações de configuração, ferramentas ou arquivos de documentação.
  * `refactor:` para alterações no código que melhoram sua estrutura sem alterar o comportamento externo.