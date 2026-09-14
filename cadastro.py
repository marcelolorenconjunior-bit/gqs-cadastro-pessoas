import re

# Listas paralelas dinâmicas
nomes = []
idades = []
emails = []

# =================================================================
# FUNÇÕES ESPECIALISTAS (REGRAS DE NEGÓCIO ISOLADAS)
# =================================================================

def classificar_faixa_etaria(idade):
    """Determina se a pessoa é criança, adolescente, adulto ou idoso."""
    if idade < 0:
        return "Idade inválida"
    elif idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

def avaliar_email(email):
    """Verifica se o e-mail está ausente, inválido ou utilizável."""
    if not email or email.strip() == "":
        return "Ausente"
    
    # Validação de formato de e-mail (presença de @ e domínio válido)
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(padrao, email):
        return "Inválido"
    
    return "Utilizável"

def identificar_provedor(email):
    """Identifica Gmail, Outlook, Hotmail, UTFPR ou outro provedor."""
    status_email = avaliar_email(email)
    if status_email != "Utilizável":
        return "Nenhum"
    
    dominio = email.split("@")[-1].lower()
    
    if "gmail.com" in dominio:
        return "Gmail"
    elif "outlook.com" in dominio:
        return "Outlook"
    elif "hotmail.com" in dominio:
        return "Hotmail"
    elif "utfpr.edu.br" in dominio:
        return "UTFPR"
    else:
        return "Outro"

def definir_condicao_contato(idade, email):
    """Determina a condição da pessoa para contato."""
    faixa = classificar_faixa_etaria(idade)
    status_email = avaliar_email(email)
    
    if faixa == "Criança":
        return "Não contatar (Menor de idade)"
    
    if status_email == "Ausente":
        return "Requer atualização de cadastro (Sem e-mail)"
    elif status_email == "Inválido":
        return "Requer correção (E-mail inválido)"
    
    if faixa == "Adolescente":
        return "Contatar com restrições"
    
    return "Pronto para contato"

# =================================================================
# FUNÇÃO PRINCIPAL DE ANÁLISE (COORDENADORA)
# =================================================================

def analisar_pessoa(nomes, idades, emails, nome_busca):
    """Localiza a pessoa e utiliza as funções anteriores para realizar a análise."""
    try:
        idx = nomes.index(nome_busca)
    except ValueError:
        return None
    
    idade = idades[idx]
    email = emails[idx]
    
    # Coordenação das chamadas delegadas
    faixa_etaria = classificar_faixa_etaria(idade)
    status_email = avaliar_email(email)
    provedor = identificar_provedor(email)
    condicao_contato = definir_condicao_contato(idade, email)
    
    return {
        "nome": nomes[idx],
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
    print("\n=========================")
    print("   CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    return int(input("Escolha uma opcao: "))

op = 0
while op != 5:
    op = exibir_menu()
    
    if op == 1:
        n = input("Nome: ")
        i = int(input("Idade: "))
        e = input("E-mail: ")
        
        nomes.append(n)
        idades.append(i)
        emails.append(e)
        
        print("\nPessoa cadastrada!")
        print("Nome: " + n)
        print("Idade: " + str(i))
        print("E-mail: " + e)
        if i >= 18:
            print("Situacao: Maior de idade")
        else:
            print("Situacao: Menor de idade")
            
    elif op == 2:
        nome_busca = input("Digite o nome completo para consulta: ")
        resultado = analisar_pessoa(nomes, idades, emails, nome_busca)
        
        if resultado is None:
            print(f"\nPessoa '{nome_busca}' não encontrada no cadastro.")
        else:
            print("\n--- RESULTADO DA ANÁLISE ---")
            print(f"Nome: {resultado['nome']}")
            print(f"Idade: {resultado['idade']} anos ({resultado['faixa_etaria']})")
            print(f"E-mail: {resultado['email']} ({resultado['status_email']})")
            print(f"Provedor Identificado: {resultado['provedor']}")
            print(f"Condição de Contato: {resultado['condicao_contato']}")
            print("----------------------------")
            
    elif op == 4:
        qtd = len(nomes)
        if qtd == 0:
            print("\nNenhuma pessoa cadastrada")
        else:
            print("\n--- LISTAGEM ---")
            for idx in range(qtd):
                print("Nome: " + nomes[idx])
                print("Idade: " + str(idades[idx]))
                print("E-mail: " + emails[idx])
                print("-------------------------")
            print("Total: " + str(qtd))
            
    elif op == 5:
        print("Saindo...")
    elif op != 3:
        print("Opcao invalida")

print("Fim do programa")
