from robot import Robot

class Fleet:
    def __init__(self) -> None:
        self.name = []
        self.add_robot_to_herd()

    def add_robot_to_herd(self):
        name1 = Robot("IG-88")
        name2 = Robot("General Greivous")
        name3 = Robot("C3PO")

        self.name.append(name1)
        self.name.append(name2)
        self.name.append(name3)

