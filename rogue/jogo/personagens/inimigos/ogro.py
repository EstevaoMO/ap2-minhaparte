import random

from .inimigo import Inimigo

class Ogro(Inimigo):
    def __init__(self):
        super().__init__()
        self.forca = random.randint(10, 25)
        self.vida = random.randint(50, 100)
        self.xp = 3
        self.nome = "Ogro"
