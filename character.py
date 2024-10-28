class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"My name is {self.name}")

    def instigate(self):
        print(f"{self.name} you stink")

    def attack(self, opponent):
        opponent.health = opponent.health - self.strength
        print(f"{self.name} attacks {opponent.name}")
        print(f"{opponent.name} has {opponent.health} health")

character = Character("Bob", 100, 50)
#print(character.name)
#print(character.health)

x = Character("Steve", 100, 50)
#print(x.name, x.health)
#print(x.health)

x.greet()
x.instigate()
while x.health > 0 and character.health > 0:
x.attack(character)
character.attack(x)
