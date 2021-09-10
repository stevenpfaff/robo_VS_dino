class Dinosaur :
    def __init__(self, attack_power) -> None:
        self.dino = ["Monty", "Rex", "Scoop"]
        self.attack_power = attack_power
        self.health = 140

    def attack(self, robot):
        robot.health = robot.health - self.attack_power
