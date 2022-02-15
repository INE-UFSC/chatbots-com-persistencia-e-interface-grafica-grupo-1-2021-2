# implemente as seguintes classes

from .Comando import Comando
from abc import ABC, abstractmethod
import random as r


class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def cria_comando(self, id, msg, respostas):
        return Comando(id, msg, respostas)

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass

    @abstractmethod
    def despedida():
        pass
