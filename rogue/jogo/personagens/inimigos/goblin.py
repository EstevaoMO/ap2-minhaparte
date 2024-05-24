import random

from .inimigo import Inimigo

class Goblin(Inimigo):
    def __init__(self):
        super().__init__()
        self.forca = random.randint(5, 15)
        self.vida = random.randint(10, 40)
        self.xp = 1
        self.nome = "Goblin"
