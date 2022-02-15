from Bots.Bot import Bot


class BotJose(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = [self.cria_comando(1, "conselho para os estudos",
                                             ["José analisa suas notas. José diz: Desistir é para os fracos, o ideal é nem tentar"]),
                           self.cria_comando(2, "conselho amoroso",
                                             ["José analisa seu Tinder. José diz: Nunca é tarde para um novo fracasso"]),
                           self.cria_comando(3, "conselho para a carreira",
                                             ["José te entrega um guia de como se comportar numa entrevista. Regra 1: chame o empregador de 'meu parça', é contrato na certa"]),
                           self.cria_comando(4, "adeus",
                                             ["José diz: Vamos esquecer os erros do passado, meu amigo, e focar nos erros do futuro. Adeus, até vista"])
                           ]

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return "Mensagem de apresentação: Olá, eu sou o José, seu bot conselheiro"

    def executa_comando(self, id):
        for comando in self.__comandos:
            if comando.id == id:
                return comando.get_resposta_random()

    def boas_vindas(self):
        return "José diz: Que bom que você me escolheu! Espero que eu possa te ajudar"

    def despedida(self):
        return(self.__comandos[-1].get_resposta_random())
