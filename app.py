#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotMusical import BotMusical

###construa a lista de bots disponíveis aqui
lista_bots = [BotMusical("Brook")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
