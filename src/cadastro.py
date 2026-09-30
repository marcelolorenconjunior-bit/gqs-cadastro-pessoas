"""Módulo contendo o gerenciamento do cadastro de pessoas."""

from src.pessoa import Pessoa

class CadastroPessoas:
    """Classe que mantém e gerencia o conjunto de pessoas cadastradas."""

    def __init__(self):
        self.__pessoas = []

    def cadastrar(self, nome, idade, email):
        """Cria uma nova pessoa e a adiciona à lista interna."""
        pessoa = Pessoa(nome, idade, email)
        self.__pessoas.append(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        """Busca uma pessoa na lista através do nome completo."""
        for pessoa in self.__pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def listar(self):
        """Retorna a lista completa com todas as pessoas cadastradas."""
        return self.__pessoas

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        """Altera os dados de uma pessoa localizada pelo nome."""
        pessoa = self.buscarPorNome(nome)
        if pessoa is None:
            return None
        
        pessoa.setNome(novo_nome)
        pessoa.setIdade(nova_idade)
        pessoa.setEmail(novo_email)
        return pessoa
