from dino import Dinosaur

class Herd:
    def __init__(self):
        self.Dinosaur = []
        self.create_herd()

    def create_herd(self):
        dino1 = Dinosaur("Scoop", 60)
        dino2 = Dinosaur("Monty", 60)
        dino3 = Dinosaur("Rex", 60)

        self.Dinosaur.append(dino1)
        self.Dinosaur.append(dino2)
        self.Dinosaur.append(dino3)
