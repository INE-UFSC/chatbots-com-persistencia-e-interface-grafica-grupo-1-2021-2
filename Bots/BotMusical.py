from Bots.Bot import Bot


class BotMusical(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = [self.cria_comando(
            1, 'Bom dia', ['Alguma coisa acontece no meu coração... Ah, oi! Bom dia!']),
            self.cria_comando(2, 'Quem é você?', [
                              f'EU SOU O SAMBAAA! Brincadeira, eu sou {self.__nome}!']),
            self.cria_comando(3, 'Como vai ser o futuro?',
                              ['Eu vejo a vida melhor no futuro, eu vejo isso por cima de um muro\nde hipocrisia que insiste em nos rodear...'
                               ]),
            self.cria_comando(4, 'Adeus', [
                              'Deixe-me ir, preciso andar, vou por aí a procurar... Rir pra não chorar! Tchaau!',
                              'Oh, sim, eu estou tão cansado, mas não pra dizer que eu tô indo embora!'])
        ]

    @property
    def comandos(self):
        return self.__comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def boas_vindas(self):
        return(self.__comandos[0].get_resposta_random())
        
    def despedida(self):
        return(self.__comandos[-1].get_resposta_random())

    def apresentacao(self):
        return f'Deixa eu me apresentar, que eu acabei de chegar! Meu nome é {self.__nome}!'

    def executa_comando(self, id):
        for comando in self.__comandos:
            if comando.id == id:
                return comando.get_resposta_random()
