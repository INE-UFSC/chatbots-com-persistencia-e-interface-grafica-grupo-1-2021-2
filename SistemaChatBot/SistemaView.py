import PySimpleGUI as sg 

# View do padrão MVC
class SistemaView():
    def __init__(self):
        self.__container = []
        self.__window = sg.Window("Sistema ChatBot", self.__container ,font=("Helvetica", 14))

    def tela_chat(self):
        linha0 = [sg.Text('Bem vindo ao sistema de chatbots')]
        linha1 = [sg.Text('')]
        linha2 = [sg.Text('Escolha seu bot: ')]
        linha3 = [sg.Button('Musical'), sg.Button('José')]
        linha4 = [sg.Text('', key='mensagem')]
        
        self.__container = [linha0, linha1, linha2, linha3, linha4]
        self.__window = sg.Window("Sistema ChatBot", self.__container ,font=("Helvetica", 14))

    def tela_bot(self):
        linha0 = [sg.Text('')] #Mensagem de apresentação do bot
        linha1 = [sg.Text('')]
        linha2 = [sg.Button(''), sg.Button(''), sg.Button(''), sg.Button(''),] #Comandos
        linha3 = [sg.Text('', key='mensagem')] 
        
        self.__container = [linha0, linha1, linha2, linha3]
        self.__window = sg.Window("", self.__container ,font=("Helvetica", 14))


    def mostra_mensagem(self, mensagem): 
        self.__window.Element('mensagem').Update(mensagem)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
