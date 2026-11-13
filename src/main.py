"""Programa principal para cadastro de pessoas. Uso didatico na disciplina de GQS."""
import os
from cadastro import CadastroPessoas
from repositorio_pessoas import RepositorioPessoas
from repositorio_pessoas_memoria import RepositorioPessoasMemoria
from repositorio_pessoas_mysql import RepositorioPessoasMySQL

USAR_MYSQL = os.getenv("USAR_MYSQL", "false").lower() == "true"


def criar_repositorio() -> RepositorioPessoas:
    """Instancia o repositorio configurado para a aplicacao."""
    if USAR_MYSQL:
        return RepositorioPessoasMySQL()
    return RepositorioPessoasMemoria()


def exibir_menu() -> int:
    """Exibe o menu principal e retorna a opcao escolhida."""
    print("\n-------------------------")
    print(" CADASTRO DE PESSOAS")
    print("-------------------------")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    return int(input("Escolha uma opcao: "))


def cadastrar_pessoa(cadastro: CadastroPessoas) -> None:
    """Le os dados e cadastra uma nova pessoa."""
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("E-mail: ")
    pessoa = cadastro.cadastrar(nome, idade, email)
    print(f"Pessoa cadastrada: {pessoa.getNome()}")


def consultar_pessoa(cadastro: CadastroPessoas) -> None:
    """Consulta uma pessoa pelo nome."""
    nome = input("Nome para consultar: ")
    pessoa = cadastro.buscarPorNome(nome)
    if pessoa is None:
        print("Pessoa nao encontrada")
    else:
        print(
            f"Nome: {pessoa.getNome()} | Idade: {pessoa.getIdade()} | E-mail: {pessoa.getEmail()}"
        )


def alterar_pessoa(cadastro: CadastroPessoas) -> None:
    """Altera os dados de uma pessoa existente."""
    nome = input("Nome para alterar: ")
    atual = cadastro.buscarPorNome(nome)
    if atual is None:
        print("Pessoa nao encontrada")
        return
    novo_nome = input("Novo nome: ")
    nova_idade = int(input("Nova idade: "))
    novo_email = input("Novo e-mail (enter para manter): ")
    alterada = cadastro.alterar(nome, novo_nome, nova_idade, novo_email)
    if alterada is not None:
        print("Cadastro alterado com sucesso!")


def listar_pessoas(cadastro: CadastroPessoas) -> None:
    """Lista todas as pessoas cadastradas."""
    pessoas = cadastro.listar()
    if not pessoas:
        print("Nenhuma pessoa cadastrada")
        return
    for pessoa in pessoas:
        print(
            f"Nome: {pessoa.getNome()} | Idade: {pessoa.getIdade()} | E-mail: {pessoa.getEmail()}"
        )
    print(f"Total: {len(pessoas)}")


def executar() -> None:
    """Executa o loop principal da aplicacao."""
    cadastro = CadastroPessoas(criar_repositorio())
    opcao = 0
    while opcao != 5:
        opcao = exibir_menu()
        if opcao == 1:
            cadastrar_pessoa(cadastro)
        elif opcao == 2:
            consultar_pessoa(cadastro)
        elif opcao == 3:
            alterar_pessoa(cadastro)
        elif opcao == 4:
            listar_pessoas(cadastro)
        elif opcao == 5:
            print("Saindo...")
        else:
            print("Opcao invalida")


if __name__ == "__main__":
    executar()
