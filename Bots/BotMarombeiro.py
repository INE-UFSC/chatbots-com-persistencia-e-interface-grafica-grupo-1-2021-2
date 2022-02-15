from Bots.Bot import Bot


class BotMarombeiro(Bot):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.__comandos = [self.cria_comando(1, "Eai frango",
                                             ["Frango é tu rapaz, tem nem 40 de braço, ta doido!?!"]),
                           self.cria_comando(2, "Me passa um treino?",
                                             ["3x10 supino\n3x10 barra fixa\n3x10 rosca direta\n3x10 tríceps testa\n(perna não precisa)"]),
                           self.cria_comando(3, "Conselho",
                                             ["Quer ficar grande? Tem que comer e treinar todo dia!"]),
                           self.cria_comando(4, "Adeus",
                                             ["Valeu mermão, até a próxima."])
                           ]

    def apresentacao(self):
        return "Treino e dieta eu não furo, tá ligado?"

    def executa_comando(self, id):
        for comando in self.__comandos:
            if comando.id == id:
                return comando.get_resposta_random()

    def boas_vindas(self):
        return "HORA DO SHOW P****!"

    def despedida(self):
        return(self.__comandos[-1].get_resposta_random())
