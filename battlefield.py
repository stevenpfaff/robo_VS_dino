from fleet import Fleet
from herd import Herd
from weapon import Weapon
from dino import Dino
from robot import Robot


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.display_winners()
    
    def display_welcome(self):
        print("Welcome to Robots Versus Dinosaurs")

    def show_dino_opponent_options(self):
        pass
    
    def show_robot_opponent_options(self):
        pass

    def dino_turn(self, Dino):
        pass
    def robot_turn(self, Robot):
        pass
    
    def display_winners(self, winner):
        if winner == "dino":
            print("Dinos Win!")
        elif winner == "robo":
            print("Robots Win!")
