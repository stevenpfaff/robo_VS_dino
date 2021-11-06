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
        for robot in self.robots.robots:
            print("Name:"f"{robot.name}")
            print("Weapon Name:"f"{robot.weapon.name}")
            print("Weapon Damage:"f"{robot.weapon.attack_power}")
            print("Health:"f"{robot.health}")
    
    def show_robot_opponent_options(self):
        for dino in self.dinosaurs.dinosaurs:
            print("Name:"f"{dino.name}")
            print("Attack Power:"f"{dino.attack_power}")
            print("Health:"f"{dino.health}")

    def dino_turn(self, Herd):
        print("select from the following dinos to attack")
        dino_choice = input(f'1:{self.Herd[0].name}, 2:{self.Herd[1].name}, 3: {self.Herd[2].name}')

    def robot_turn(self, Fleet):
        print("select from the following robots to attack")
        dino_choice = input(f'1:{self.Fleet[0].name}, 2:{self.Fleet[1].name}, 3: {self.Fleet[2].name}')
    
    def display_winners(self, winner):
        if winner == "dino":
            print("Dinos Win!")
        elif winner == "robo":
            print("Robots Win!")
