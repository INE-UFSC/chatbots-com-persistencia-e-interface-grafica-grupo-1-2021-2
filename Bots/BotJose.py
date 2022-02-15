from Bots.Bot import Bot

class BotJose(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {
            "1": "conselho para os estudos",
            "2": "conselho amoroso",
            "3": "conselho para a carreira",
            "4": "adeus"}
    @property
    def comandos(self):
        return self.__comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return "Mensagem de apresentação: Olá, eu sou o José, seu bot conselheiro"
 
    def mostra_comandos(self):
        print("1 - conselho para os estudos")
        print("2 - conselho amoroso")
        print("3 - conselho para a carreira")
    def executa_comando(self,cmd):
        if cmd == 1:
            self.conselho_estudos()
        elif cmd == 2:
           self.conselho_amoroso()
        elif cmd == 3:
          self.conselho_carreira()
        else:
           self.despedida() 
            
    def conselho_estudos(self):
        return "José analisa suas notas. José diz: Desistir é para os fracos, o ideal é nem tentar"
    
    def conselho_amoroso(self):
        return "José analisa seu Tinder. José diz: Nunca é tarde para um novo fracasso"
    
    def conselho_carreira(self):
        return "José te entrega um guia de como se comportar numa entrevista. Regra 1: chame o empregador de 'meu parça', é contrato na certa"

    def boas_vindas(self):
        return "José diz: Que bom que você me escolheu! Espero que eu possa te ajudar"

    def despedida(self):
        return "José diz: Vamos esquecer os erros do passado, meu amigo, e focar nos erros do futuro. Adeus, até vista"
    
