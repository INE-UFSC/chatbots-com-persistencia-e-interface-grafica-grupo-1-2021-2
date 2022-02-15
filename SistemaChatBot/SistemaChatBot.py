from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots = []
        for bot in lista_bots:
            if isinstance(bot,Bot):
                self.__lista_bots.append(bot)
            else:
                raise ValueError('Um dos bots inseridos nao pertence a classe Bot')
        self.__bot = None
    
    def boas_vindas(self):
        print(f'Bom dia, bem vindo ao sistema de chatbots da empresa {self.empresa}!\n')

    def mostra_menu(self):
        print('Bots disponíveis:')
        for i,bot in enumerate(self.lista_bots):
            print(f'{i+1} - {bot.nome} - Apresentação: {bot.apresentacao()}')

    
    def escolhe_bot(self):
        while True:
            escolha = input('Digite o numero do bot desejado, ou -1 para sair: ')
            try: 
                escolha = int(escolha)
            except: 
                print('A escolha precisa ser um número inteiro.')
                continue

            if escolha-1 >= 0 and escolha-1 < len(self.lista_bots):
                self.bot = self.lista_bots[escolha-1]
                return True
            elif escolha == -1:
                return False
            else:
                print('Insira um índice de um bot que exista')

    def mostra_comandos_bot(self):
        for cm in self.__bot.comandos:
            print(f'{cm.id} - {cm.mensagem}')

    def le_envia_comando(self):
        while True:
            escolha = input('Digite o numero do comando desejado (ou -1 para sair): ')
            try: 
                escolha = int(escolha)
            except: 
                print('A escolha precisa ser um número inteiro.')
                continue

            if escolha == -1:
                return False
            else:
                for cm in self.__bot.comandos:
                    if escolha == cm.id:
                        print(self.__bot.executa_comando(escolha))
                        return True
                print('Insira um índice de um bot que exista')

    def inicio(self):
        self.boas_vindas() #mostra a tela de boas vindas
        while True:
            self.mostra_menu() #mostra o menu com os bots disponiveis
            if not self.escolhe_bot(): #o usuario escolhe um bot da lista de bots
                break
            print(self.__bot.boas_vindas()) #imprime a mensagem de boas vindas do bot
            while True: #entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
                self.mostra_comandos_bot()
                if not self.le_envia_comando():
                    print(self.bot.despedida()) #ao sair mostra a mensagem de despedida do bot
                    break
    
    @property
    def empresa(self): return(self.__empresa)

    @property
    def lista_bots(self): return(self.__lista_bots)

    @property
    def bot(self): return(self.__bot)

    @bot.setter
    def bot(self, bot): self.__bot = bot
