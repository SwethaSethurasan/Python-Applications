class Character:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def display(self):
        print("Name:",self.name)
        print("Health:",self.health)
    def move(self):
        print(f"{self.name} is moving")
    def attack(self):
        print(f"{self.name} is attacking 🗡")
    def take_damage(self):
        print(f"Damage has done by {self.name}")
class Player(Character):
    def __init__(self,name,health,points):
        super().__init__(name,health)
        self.points=points
    def get_points(self):
        print("Points:",self.points)
    def buy(self):
        print(f"{self.name} bought a weapon 🗡")
    def spell(self,spell):
        self.spell=spell
        print(f"{self.spell} is casted 🪄")
class NPC(Character):
    def __init__(self,name,health):
        super().__init__(name,health)
    def dialogue(self):
        diag=input("Enter a dialogue:")
        print(diag)
    def quests(self):
        quest=input("Enter a quest:")
        print(f"{quest}♦ is found")
    def trading(self):
        print("Trading is started")
class Monster(Player):
    def __init__(self,monster,name,health,points):
        super().__init__(name,health,points)
        self.monster=monster
    def get_points(self):
        print("Points:",self.points)
    def attack(self):
        print(f"{self.monster} is attacking 🗡 {self.name}")
 
def __main__():
    print("-----------*Virtual World*------------")
    print("-----Player------")
    p1=Player("Ganguli",60,120)  
    p1.display()
    p1.get_points()
    p1.buy()
    p1.move()
    p1.attack()
    p1.spell("jump")
    p1.take_damage()
    print("-----NPC------")
    n1=NPC("Nayan",70)
    n1.display()
    n1.dialogue()
    n1.quests()
    n1.trading()
    print("-----Monster------")
    m1=Monster("Godzilla","Ganguli",90,150)
    m1.get_points()
    m1.move()
    m1.attack()

if __name__==__main__():
    main()
