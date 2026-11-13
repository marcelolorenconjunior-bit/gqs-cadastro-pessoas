"""Implementacao em memoria do repositorio de pessoas."""
from typing import List, Optional
from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMemoria(RepositorioPessoas):
    """Armazena as pessoas cadastradas em uma lista em memoria."""

    def __init__(self) -> None:
        """Inicializa a lista vazia de pessoas."""
        self.__pessoas: List[Pessoa] = []

    def cadastrar(self, pessoa: Pessoa) -> None:
        """Adiciona uma pessoa na lista em memoria."""
        self.__pessoas.append(pessoa)

    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Busca uma pessoa pelo nome na lista em memoria."""
        for pessoa in self.__pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def listar(self) -> List[Pessoa]:
        """Retorna uma copia da lista de pessoas cadastradas."""
        return list(self.__pessoas)

    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Atualiza os dados da pessoa encontrada pelo nome."""
        pessoa = self.buscar(nome)
        if pessoa is None:
            return False
        pessoa.setNome(nova_pessoa.getNome())
        pessoa.setIdade(nova_pessoa.getIdade())
        if nova_pessoa.getEmail() != "":
            pessoa.setEmail(nova_pessoa.getEmail())
        return True
