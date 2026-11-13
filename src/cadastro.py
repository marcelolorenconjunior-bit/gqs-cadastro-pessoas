"""Modulo de regras de negocio do Cadastro de Pessoas."""
from typing import List, Optional
from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas
from repositorio_pessoas_memoria import RepositorioPessoasMemoria


class CadastroPessoas:
    """Gerencia as operacoes de cadastro utilizando um repositorio."""

    def __init__(self, repositorio: Optional[RepositorioPessoas] = None) -> None:
        """Inicializa o cadastro com o repositorio informado ou em memoria."""
        self.__repositorio = repositorio or RepositorioPessoasMemoria()

    def cadastrar(self, nome: str, idade: int, email: str) -> Pessoa:
        """Cria e registra uma nova pessoa no repositorio."""
        pessoa = Pessoa(nome, idade, email)
        self.__repositorio.cadastrar(pessoa)
        return pessoa

    def buscarPorNome(self, nome: str) -> Optional[Pessoa]:
        """Consulta uma pessoa pelo nome no repositorio."""
        return self.__repositorio.buscar(nome)

    def listar(self) -> List[Pessoa]:
        """Retorna todas as pessoas cadastradas no repositorio."""
        return self.__repositorio.listar()

    def alterar(
        self, nome: str, novo_nome: str, nova_idade: int, novo_email: str
    ) -> Optional[Pessoa]:
        """Atualiza os dados de uma pessoa e persiste a alteracao no repositorio."""
        atual = self.__repositorio.buscar(nome)
        if atual is None:
            return None
        email_final = novo_email if novo_email != "" else atual.getEmail()
        nova_pessoa = Pessoa(novo_nome, nova_idade, email_final)
        if self.__repositorio.alterar(nome, nova_pessoa):
            return self.__repositorio.buscar(novo_nome)
        return None
