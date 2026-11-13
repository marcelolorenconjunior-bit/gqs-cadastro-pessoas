"""Programa para cadastro de pessoas. Uso didatico na disciplina de GQS."""

from cadastro import CadastroPessoas

def exibir_menu():
    """Exibe o menu principal."""
    print("\n=========================")
    print("   CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Avaliar cadastro")
    print("6 - Sair")
    return int(input("Escolha uma opcao: "))

def cadastrar_pessoa(cadastro):
    """Cadastra uma nova pessoa."""
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    email = input("Informe o email: ")

    cadastro.cadastrar(nome, idade, email)

    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def exibir_pessoa(pessoa):
    """Exibe os dados de uma pessoa."""
    print(f"Nome: {pessoa.getNome()}")
    print(f"Idade: {pessoa.getIdade()}")
    print(f"E-mail: {pessoa.getEmail()}")
    if pessoa.getIdade() >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def consultar_pessoa(cadastro):
    """Consulta uma pessoa pelo nome."""
    procurado = input("Nome para consultar: ")
    pessoa = cadastro.buscarPorNome(procurado)

    if pessoa is None:
        print("Nome nao encontrado")
    else:
        exibir_pessoa(pessoa)

def alterar_pessoa(cadastro):
    """Altera os dados de uma pessoa."""
    procurado = input("Nome para alterar: ")
    pessoa = cadastro.buscarPorNome(procurado)

    if pessoa is None:
        print("Nome nao encontrado")
    else:
        novo_nome = input("Input('Novo nome: ")
        nova_idade = int(input("Input('Nova idade: "))
        novo_email = input("Input('Novo e-mail: ")
        cadastro.alterar(procurado, novo_nome, nova_idade, novo_email)
        print("Pessoa alterada!")

def listar_pessoas(cadastro):
    """Lista todas as pessoas cadastradas."""
    pessoas = cadastro.listar()

    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada")
        return

    for pessoa in pessoas:
        exibir_pessoa(pessoa)
        print("-------------------------")

    print(f"Total: {len(pessoas)}")

def analisar_faixa_etaria(idade):
    """Analisa a faixa etaria."""
    if idade < 12:
        print("Faixa etaria: crianca")
    elif idade < 18:
        print("Faixa etaria: adolescente")
    elif idade < 60:
        print("Faixa etaria: adulto")
    else:
        print("Faixa etaria: idoso")

def analisar_contato(idade, email):
    """Analisa as informacoes de contato."""
    if idade >= 18 and "@" in email:
        print("Contato: completo")
    elif idade >= 18:
        print("Contato: e-mail invalido")
    else:
        print("Contato: menor de idade")

def analisar_pessoa(cadastro):
    """Analisa os dados de uma pessoa."""
    procurado = input("Nome para analisar: ")
    pessoa = cadastro.buscarPorNome(procurado)

    if pessoa is None:
        print("Pessoa nao encontrada")
    else:
        analisar_faixa_etaria(pessoa.getIdade())
        analisar_contato(pessoa.getIdade(), email=pessoa.getEmail())

def executar():
    """Executa o menu principal da aplicacao."""
    cadastro = CadastroPessoas()
    op = 0

    while op != 6:
        op = exibir_menu()

        if op == 1:
            cadastrar_pessoa(cadastro)
        elif op == 2:
            consultar_pessoa(cadastro)
        elif op == 3:
            alterar_pessoa(cadastro)
        elif op == 4:
            listar_pessoas(cadastro)
        elif op == 5:
            analisar_pessoa(cadastro)
        elif op == 6:
            print("Saindo...")
        else:
            print("Opcao invalida")

    print("Fim do programa")

if __name__ == "__main__":
    executar()
