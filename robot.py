from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = [Weapon("Lightsaber", 80), Weapon("Rocket Launcher", 60), Weapon("Laser", 40)]

        def attack(self, dinosaur):
            weapon_option = input(
                "Choose a weapon \nEnter 0 for Lightsaber, 1 for Rocket Launcher, 2 for Laser: "
            )
            if weapon_option == "0":
                dinosaur.health = dinosaur.health - self.weapon[0].attack_power
            elif weapon_option == "1":
                dinosaur.health = dinosaur.health - self.weapon[1].attack_power
            elif weapon_option == "2":
                dinosaur.health = dinosaur.health - self.weapon[2].attack_power
        
        
