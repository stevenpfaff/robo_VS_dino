from fleet import Fleet
from herd import Herd
from weapon import Weapon
from dino import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        pass
    
    def display_welcome(self):
        print("Welcome to Robots Versus Dinosaurs")

    def show_dino_opponent_options(self):
        print(Herd())
    
    def show_robot_opponent_options(self):
        print(Fleet())

    def dino_turn(self, Dinosaur):
           print(
            "Which Robot would you like to attack?\nIG-88: Health=100 ",
            self.fleet.robots[0].health,
            "\nGeneral: Health=100 ",
            self.fleet.robots[1].health,
            "\nR2D2: Health=100 ",
            self.fleet.robots[2].health,
        )

    def robot_turn(self, Robot):
        print(
            "Which Dinosaur would you like to attack?\nScoop: Health=60 ",
            self.herd.dinosaurs[0].health,
            "\nMonty: Health=60 ",
            self.herd.dinosaurs[1].health,
            "\nRex: Health=60 ",
            self.herd.dinosaurs[2].health,
        )
    
    def display_winners(self, winner):
        if winner == "dino":
            print("Dinos Win!")
        elif winner == "robo":
            print("Robots Win!")
