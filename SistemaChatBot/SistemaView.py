import PySimpleGUI as sg 

# View do padrão MVC
class SistemaView():
    def __init__(self):
        self.__container = []
        self.__window = sg.Window("Sistema ChatBot", self.__container ,font=("Helvetica", 14))

    def tela_chat(self, bots):
        linha0 = [sg.Text('Bem vindo ao sistema de chatbots')]
        linha1 = [sg.Text('')]
        linha2 = [sg.Text('Escolha seu bot: ')]
        linha3 = []
        for bot in bots:
            linha3.append(sg.Button(bot.nome))
        linha4 = [sg.Text('', key='mensagem')]
        
        self.__container = [linha0, linha1, linha2, linha3, linha4]
        self.__window = sg.Window("Sistema ChatBot", self.__container ,font=("Helvetica", 14))

    def tela_bot(self, bot):
        linha0 = [sg.Text(bot.apresentacao())] #Mensagem de apresentação do bot
        linha1 = [sg.Text('')]
        linha2 = [] #Comandos
        for cmd in bot.comandos:
            linha2.append(sg.Button(cmd.mensagem))
        linha3 = [sg.Text('', key='mensagem')] 
        
        self.__container = [linha0, linha1, linha2, linha3]
        self.__window = sg.Window("", self.__container ,font=("Helvetica", 14))


    def mostra_mensagem(self, mensagem): 
        self.__window.Element('mensagem').Update(mensagem)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
