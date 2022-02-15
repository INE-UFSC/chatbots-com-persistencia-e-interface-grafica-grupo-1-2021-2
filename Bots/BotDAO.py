from .DAO import DAO

class BotDAO(DAO):
    def __init__(self):
        super().__init__('bots.pkl')

    #adiciona bots com base no local do arquivo
    def importBot(self, local_arquivo_bot):
        pass

    #escreve o bot num arquivo separado
    def exportBot(self, nome_bot):
        pass