from random import randrange
class Comando():
    def __init__(self, id:int, msg:str, respostas:list):
        self.__id = int(id)
        self.__mensagem = msg
        self.__respostas = respostas

    @property
    def id(self)->int:
        return self.__id

    @property
    def mensagem(self)->str:
        return self.__mensagem

    def get_resposta_random(self)->str:
        return self.__respostas[randrange(len(self.__respostas))]
