"""Testes automatizados para o Cadastro de Pessoas."""
from cadastro import CadastroPessoas


def test_cadastrar_e_buscar_pessoa():
    """Testa o cadastro de uma pessoa e a busca por nome."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Maria Silva", 25, "maria@email.com")

    encontrada = cadastro.buscarPorNome("Maria Silva")
    assert encontrada is not None
    assert encontrada.getNome() == "Maria Silva"
    assert encontrada.getIdade() == 25


def test_buscar_pessoa_inexistente():
    """Testa a busca por um nome que nao esta cadastrado."""
    cadastro = CadastroPessoas()
    assert cadastro.buscarPorNome("Joao Ninguem") is None


def test_alterar_pessoa():
    """Testa a alteracao dos dados de uma pessoa cadastrada."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Carlos", 30, "carlos@email.com")

    alterada = cadastro.alterar("Carlos", "Carlos Souza", 31, "carlos.souza@email.com")

    assert alterada is not None
    atualizada = cadastro.buscarPorNome("Carlos Souza")
    assert atualizada is not None
    assert atualizada.getIdade() == 31


def test_listar_pessoas():
    """Testa a listagem de pessoas cadastradas."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Lucas", 22, "lucas@email.com")
    cadastro.cadastrar("Julia", 27, "julia@email.com")

    lista = cadastro.listar()
    assert len(lista) == 2
    assert lista[0].getNome() == "Lucas"
    assert lista[1].getNome() == "Julia"
