from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robot = []
        self.create_fleet()

    def create_fleet(self):
        robo1 = Robot("IG-88")
        robo2 = Robot("General")
        robo3 = Robot("R2D2")

        self.robot.append(robo1)
        self.robot.append(robo2)
        self.robot.append(robo3)
