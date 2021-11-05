from robot import Robot

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 80
        self.attack_power = attack_power
        

    def attack(self, robot):
        robot.health = robot.health - self.attack_power