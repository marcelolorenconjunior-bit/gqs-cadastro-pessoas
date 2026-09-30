"""
Módulo de Gestão de Cadastro de Pessoas.
COM1024 - Gestão da Qualidade de Software - UTFPR Medianeira.
"""
import re

# Listas paralelas dinâmicas globais
NOMES = []
IDADES = []
EMAILS = []

# =================================================================
# FUNÇÕES ESPECIALISTAS (REGRAS DE NEGÓCIO ISOLADAS)
# =================================================================

def classificar_faixa_etaria(idade):
    """
    Determina se a pessoa é criança, adolescente, adulto jovem, adulto ou idoso.
    """
    if idade < 0:
        return "Idade inválida"
    if idade <= 12:
        return "Criança"
    if idade <= 17:
        return "Adolescente"
    if idade <= 24:
        return "Adulto jovem"
    if idade <= 59:
        return "Adulto"
    return "Idoso"

def avaliar_email(email):
    """
    Verifica se o e-mail está ausente, inválido ou utilizável.
    """
    if not email or email.strip() == "":
        return "Ausente"

    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(padrao, email):
        return "Inválido"

    return "Utilizável"

def identificar_provedor(email):
    """
    Identifica Gmail, Outlook, Hotmail, UTFPR ou outro provedor.
    """
    status_email = avaliar_email(email)
    if status_email != "Utilizável":
        return "Nenhum"

    dominio = email.split("@")[-1].lower()

    if "gmail.com" in dominio:
        return "Gmail"
    if "outlook.com" in dominio:
        return "Outlook"
    if "hotmail.com" in dominio:
        return "Hotmail"
    if "utfpr.edu.br" in dominio:
        return "UTFPR"
    return "Outro"

def definir_condicao_contato(idade, email):
    """
    Determina a condição da pessoa para contato com base na idade e e-mail.
    """
    faixa = classificar_faixa_etaria(idade)
    status_email = avaliar_email(email)

    if faixa == "Criança":
        return "Não contatar (Menor de idade)"

    if status_email == "Ausente":
        return "Requer atualização de cadastro (Sem e-mail)"
    if status_email == "Inválido":
        return "Requer correção (E-mail inválido)"

    if faixa == "Adolescente":
        return "Contatar com restrições"

    return "Pronto para contato"

# =================================================================
# FUNÇÃO PRINCIPAL DE ANÁLISE (COORDENADORA)
# =================================================================

def analisar_pessoa(nomes_lista, idades_lista, emails_lista):
    """
    Função coordenadora. Localiza a pessoa e delega as validações.
    """
    nome_busca = input("Digite o nome completo para consulta: ")

    try:
        idx = nomes_lista.index(nome_busca)
    except ValueError:
        return None

    idade = idades_lista[idx]
    email = emails_lista[idx]

    faixa_etaria = classificar_faixa_etaria(idade)
    status_email = avaliar_email(email)
    provedor = identificar_provedor(email)
    condicao_contato = definir_condicao_contato(idade, email)

    return {
        "nome": nomes_lista[idx],
        "idade": idade,
        "email": email,
        "faixa_etaria": faixa_etaria,
        "status_email": status_email,
        "provedor": provedor,
        "condicao_contato": condicao_contato
    }

# =================================================================
# INTERFACE DO USUÁRIO E MENU
# =================================================================

def exibir_menu():
    """
    Exibe as opções do sistema na tela e captura a opção escolhida.
    """
    print("\n=========================")
    print("   CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    return int(input("Escolha uma opcao: "))

def main():
    """
    Fluxo principal do menu da aplicação.
    """
    op = 0
    while op != 5:
        op = exibir_menu()

        if op == 1:
            n = input("Nome: ")
            i = int(input("Idade: "))
            e = input("E-mail: ")

            NOMES.append(n)
            IDADES.append(i)
            EMAILS.append(e)

            print("\nPessoa cadastrada!")
            print("Nome: " + n)
            print("Idade: " + str(i))
            print("E-mail: " + e)
            if i >= 18:
                print("Situacao: Maior de idade")
            else:
                print("Situacao: Menor de idade")

        elif op == 2:
            resultado = analisar_pessoa(NOMES, IDADES, EMAILS)

            if resultado is None:
                print("\nPessoa não encontrada no cadastro.")
            else:
                print("\n--- RESULTADO DA ANÁLISE ---")
                print(f"Nome: {resultado['nome']}")
                print(f"Idade: {resultado['idade']} anos ({resultado['faixa_etaria']})")
                print(f"E-mail: {resultado['email']} ({resultado['status_email']})")
                print(f"Provedor Identificado: {resultado['provedor']}")
                print(f"Condição de Contato: {resultado['condicao_contato']}")
                print("----------------------------")

        elif op == 4:
            qtd = len(NOMES)
            if qtd == 0:
                print("\nNenhuma pessoa cadastrada")
            else:
                print("\n--- LISTAGEM ---")
                for idx in range(qtd):
                    print("Nome: " + NOMES[idx])
                    print("Idade: " + str(IDADES[idx]))
                    print("E-mail: " + EMAILS[idx])
                    print("-------------------------")
                print("Total: " + str(qtd))

        elif op == 5:
            print("Saindo...")
        elif op != 3:
            print("Opcao invalida")

if __name__ == "__main__":
    main()
    