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

class SuperHero(Hero):
    def __init__(self, name, levsl, race, magiclevel):
        super().__init__(name, levsl, race)
        self.magiclevel = magiclevel
        self.magic = 100
    def makemagic(self):
        self.magic -=10

    def show_hero(self):
        discription = (self.name + " Level is : " + str(self.level) + " Race is : " + self.race + "Helth is: " + str(self.health) + " Magic is: " + str(self.magic) ).title()
        print(discription)


myhero1 = Hero("Ben", 10, "Elf")
myhero2 = Hero("Jack", 11, "Human")
myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()

mysuperhero = SuperHero("Hary", 10, "Human", 5)
mysuperhero.show_hero()
mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.show_hero()


