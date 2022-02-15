from DAO import DAO

class BotDAO(DAO):
    def __init__(self):
        super().__init__('bots.pkl')
