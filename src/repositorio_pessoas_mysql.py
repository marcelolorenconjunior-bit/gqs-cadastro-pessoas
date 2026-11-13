"""Implementacao MySQL do repositorio de pessoas."""
import os
from typing import List, Optional
import mysql.connector
from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMySQL(RepositorioPessoas):
    """Persiste e consulta pessoas em um banco de dados MySQL."""

    def __init__(self) -> None:
        """Carrega os parametros de conexao a partir de variaveis de ambiente."""
        self.__host = os.getenv("DB_HOST", "127.0.0.1")
        self.__port = int(os.getenv("DB_PORT", "3307"))
        self.__user = os.getenv("DB_USER", "root")
        self.__password = os.getenv("DB_PASSWORD", "root")
        self.__database = os.getenv("DB_NAME", "cadastro")

    def _conectar(self):
        """Abre e retorna uma nova conexao com o MySQL."""
        return mysql.connector.connect(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database,
        )

    def cadastrar(self, pessoa: Pessoa) -> None:
        """Insere uma nova pessoa na tabela pessoa."""
        sql = "INSERT INTO pessoa (nome, idade, email) VALUES (%s, %s, %s)"
        valores = (pessoa.getNome(), pessoa.getIdade(), pessoa.getEmail())
        conexao = self._conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            conexao.commit()
        finally:
            conexao.close()

    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Consulta uma pessoa pelo nome no banco MySQL."""
        sql = "SELECT nome, idade, email FROM pessoa WHERE nome = %s LIMIT 1"
        conexao = self._conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, (nome,))
            linha = cursor.fetchone()
            if linha is None:
                return None
            return Pessoa(str(linha[0]), int(linha[1]), str(linha[2]))
        finally:
            conexao.close()

    def listar(self) -> List[Pessoa]:
        """Retorna todas as pessoas cadastradas no banco MySQL."""
        sql = "SELECT nome, idade, email FROM pessoa ORDER BY id"
        conexao = self._conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            linhas = cursor.fetchall()
            return [Pessoa(str(l[0]), int(l[1]), str(l[2])) for l in linhas]
        finally:
            conexao.close()

    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Atualiza os dados de uma pessoa existente no banco MySQL."""
        sql = "UPDATE pessoa SET nome = %s, idade = %s, email = %s WHERE nome = %s"
        valores = (
            nova_pessoa.getNome(),
            nova_pessoa.getIdade(),
            nova_pessoa.getEmail(),
            nome,
        )
        conexao = self._conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            conexao.commit()
            return cursor.rowcount > 0
        finally:
            conexao.close()
