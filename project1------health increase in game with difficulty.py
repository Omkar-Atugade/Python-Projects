import random

health = 50

x = int(input('difficulty : '))

potion_health = int(random.randint(25,50) / x)

health = health + potion_health

print(health)


