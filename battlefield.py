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
        pass

    def robot_turn(self, Robot):
        pass
    
    def display_winner(self):
        print("Robo/Dino Wins!")
