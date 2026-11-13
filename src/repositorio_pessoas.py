"""Contrato de persistencia para o Cadastro de Pessoas."""
from abc import ABC, abstractmethod
from typing import List, Optional
from pessoa import Pessoa


class RepositorioPessoas(ABC):
    """Interface abstrata que define as operacoes de persistencia."""

    @abstractmethod
    def cadastrar(self, pessoa: Pessoa) -> None:
        """Persiste uma nova pessoa no repositorio."""

    @abstractmethod
    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Busca e retorna uma pessoa pelo nome."""

    @abstractmethod
    def listar(self) -> List[Pessoa]:
        """Retorna a lista de todas as pessoas cadastradas."""

    @abstractmethod
    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Altera os dados de uma pessoa existente."""
