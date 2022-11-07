class Hero():
    """Class to create hero for our game"""
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        discription = (self.name + " Level is : " + str(self.level) + " Race is : " + self.race + "Helth is: " + str(self.health)).title()
        print(discription)

    def level_up(self):
        self.level +=1

    def move(self):
        print("Hero " + self.name + " start moveng...")

myhero1 = Hero("Ben", 10, "Elf")
myhero2 = Hero("Jack", 11, "Human")
myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()

