import random

class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.is_alive = True

    def greet(self):
        print(f"My name is {self.name}")

    def instigate(self):
        print(f"{self.name} you stink")

    def attack(self, opponent):
        opponent.health = opponent.health - ( random.randint(0, 100) % self.strength)
        if (opponent.health < 0):
            opponent.is_alive = False
        else:
            print(f"{self.name} attacks {opponent.name}")
            print(f"{opponent.name} has {opponent.health} health")

character = Character("Bob", 100, 25)
#print(character.name)
#print(character.health)

x = Character("Steve", 100, 25)
#print(x.name, x.health)
#print(x.health)

x.greet()
x.instigate()
while x.health > 0 and character.health > 0:
    if (random.randrange(0,2)) == 0:
        x.attack(character)
        if character.is_alive:
            character.attack(x)
    else:
        character.attack(x)
        if x.is_alive:
            x.attack(character)

if x.health > character.health:
    print(f"{x.name} wins!")
else:
    print(f"{character.name} wins!")