import pickle
from abc import ABC

class DAO(ABC):
    def __init__(self, local_arquivo=''):
        self.__local_arquivo = local_arquivo
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __load(self):
        self.__cache = pickle.load(open(self.__local_arquivo, 'rb'))
    
    def __dump(self):
        pickle.dump(self.__cache, open(self.__local_arquivo, 'wb'))

    def add(self, chave, obj):
        self.__cache[chave] = obj
        self.__dump()

    def get(self, chave):
        return self.__cache[chave]

    def getAll(self):
        return self.__cache

    def remove(self, chave):
        self.__cache.pop(chave)
        self.__dump