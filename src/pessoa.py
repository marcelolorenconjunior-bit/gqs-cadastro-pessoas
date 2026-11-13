"""MÃ³dulo contendo a classe Pessoa."""

class Pessoa:
    """Classe que representa uma pessoa com estado privado."""

    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    def getNome(self):
        """Retorna o nome da pessoa."""
        return self.__nome

    def getIdade(self):
        """Retorna a idade da pessoa."""
        return self.__idade

    def getEmail(self):
        """Retorna o e-mail da pessoa."""
        return self.__email

    def setNome(self, nome):
        """Define um novo nome para a pessoa."""
        self.__nome = nome

    def setIdade(self, idade):
        """Define uma nova idade para a pessoa."""
        self.__idade = idade

    def setEmail(self, email):
        """Define um novo e-mail para a pessoa."""
        self.__email = email
