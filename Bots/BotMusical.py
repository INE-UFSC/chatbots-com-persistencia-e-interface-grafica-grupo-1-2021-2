from Bots.Bot import Bot


class BotMusical(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = [self.cria_comando(
            1, 'Bom dia', ['Alguma coisa acontece no meu coração... Ah, oi! Bom dia!']),
            self.cria_comando(2, 'Quem é você?', [
                              f'EU SOU O SAMBAAA! Brincadeira, eu sou {self.nome}!']),
            self.cria_comando(3, 'Como vai ser o futuro?',
                              ['Eu vejo a vida melhor no futuro, eu vejo isso por cima de um muro\nde hipocrisia que insiste em nos rodear...',
                               'Sei que nada será como está, amanhã ou depois de amanhã...'
                               ]),
            self.cria_comando(4, 'Adeus', [
                              'Deixe-me ir, preciso andar, vou por aí a procurar... Rir pra não chorar! Tchaau!',
                              'Oh, sim, eu estou tão cansado, mas não pra dizer que eu tô indo embora!'])
        ]

    @property
    def comandos(self):
        return self.__comandos

    def boas_vindas(self):
        return(self.__comandos[0].get_resposta_random())

    def despedida(self):
        return(self.__comandos[-1].get_resposta_random())

    def apresentacao(self):
        return f'Deixa eu me apresentar, que eu acabei de chegar! Meu nome é {self.nome}!'

    def executa_comando(self, id):
        for comando in self.__comandos:
            if comando.id == id:
                return comando.get_resposta_random()

    def executa_comando_mensagem(self, mensagem):
        for comando in self.__comandos:
            if comando.mensagem == mensagem:
                return comando.get_resposta_random()
