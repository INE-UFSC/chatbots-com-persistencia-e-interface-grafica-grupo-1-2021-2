from Bots.Bot import Bot


class BotMarombeiro(Bot):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__comandos = {
            "Eai frango": "Frango é tu rapaz, tem nem 40 de braço, ta doido!?!",
            "Me passa um treino?": "3x10 supino\n3x10 barra fixa\n3x10 rosca direta\n3x10 tríceps testa\n(perna não precisa)",
            "Conselho": "Quer ficar grande? Tem que comer e treinar todo dia!"
        }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return "Treino e dieta eu não furo, tá ligado?"

    def executa_comando(self, cmd):
        try:
            return self.__comandos[cmd]
        except:
            print("Ah isso eu não sei...")

    def boas_vindas(self):
        return "HORA DO SHOW P****!"

    def despedida(self):
        return "Valeu mermão, até a próxima."
