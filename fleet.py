from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robot_one = Robot("General Grevious", Weapon)
        self.robot_two = Robot("IG-88", Weapon)
        self.robot_three = Robot("C3PO", Weapon)

        self.weapon_one = Weapon("Lightsaber")
        self.weapon_two = Weapon("Blaster")
        self.weapon_three = Weapon("Laser")