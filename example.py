import os
from game_of_life.map import Map

m = Map(20, 20)

m.getCell(5,5).changeState()
m.getCell(5,6).changeState()
m.getCell(6,6).changeState()
m.getCell(6,7).changeState()
m.getCell(7,6).changeState()

os.system('cls' if os.name == 'nt' else 'clear')
m.print()
while(1):
    answer = input("Next iteration? yes/no ")
    if answer == 'yes' or answer == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            m.update()
            m.print()
    elif answer == 'no' or answer == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
