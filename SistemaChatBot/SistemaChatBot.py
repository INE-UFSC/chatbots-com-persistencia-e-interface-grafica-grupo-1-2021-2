from Bots.Bot import Bot
from Bots.BotDAO import BotDAO
from .SistemaView import SistemaView
import PySimpleGUI as sg

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.bot_dao = BotDAO()
        for bot in lista_bots:
            if isinstance(bot,Bot):
                self.bot_dao.add(bot.nome, bot)
                self.bot_dao.remove(None)
                print(self.bot_dao.getAll())
            else:
                raise ValueError('Um dos bots inseridos nao pertence a classe Bot')
        self.__tela = SistemaView()
        self.__bot = None
    
    def boas_vindas(self):
        print(f'Bom dia, bem vindo ao sistema de chatbots da empresa {self.empresa}!\n')

    def mostra_menu(self):
        print('Bots disponíveis:')
        for i,bot in enumerate(self.bot_dao.getAll()):
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
        self.__tela.tela_chat(self.bot_dao.getAll().values()) #mostra a tela de boas vindas
        while True:
            event, values = self.__tela.le_eventos()
            if event == sg.WIN_CLOSED:
                break
            for k in self.bot_dao.getAll().keys():
                if event == k:
                    self.__bot = self.bot_dao.get(k)
                    self.__tela.tela_bot(self.__bot)
                    break
            if self.__bot != None:
                for cmd in self.__bot.comandos:
                    if event == cmd.mensagem:
                        self.__tela.mostra_mensagem(self.__bot.executa_comando_mensagem(event))

        

        self.__tela.fim()

            
    
    @property
    def empresa(self): return(self.__empresa)

    @property
    def lista_bots(self): return(self.__lista_bots)

    @property
    def bot(self): return(self.__bot)

    @bot.setter
    def bot(self, bot): self.__bot = bot
