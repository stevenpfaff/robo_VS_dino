from dino import Dino

class Herd:
    def __init__(self):
        self.Dinosaur = []
        self.create_herd()

    def create_herd(self):
        dino1 = Dino("Scoop", 60)
        dino2 = Dino("Monty", 60)
        dino3 = Dino("Rex", 60)

        self.Dinosaur.append(dino1)
        self.Dinosaur.append(dino2)
        self.Dinosaur.append(dino3)
