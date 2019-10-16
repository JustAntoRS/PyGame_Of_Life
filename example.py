import os
from game_of_life.map import Map

os.system('cls' if os.name == 'nt' else 'clear')

#Map creation
row_num = int(input('Choose the number of rows of the cell matrix: '))
column_num = int(input('Choose the number of columns of the cell matrix: '))
print('This is your matrix:')
m = Map(row_num, column_num)
m.print()

input('Press something to continue')
os.system('cls' if os.name == 'nt' else 'clear')
#Init cells in gen 0
while 1:
    m.print()
    print('Choose which cells should be alive in generation 0')
    print('Format: 0 < row_position < ' + str(row_num) + ', 0 < column_position <' + str(column_num))
    print('Example: 5,6 represents Cell at position matrix[5][6]')
    print('When you are done creating born cells, write DONE')
    inp = input()
    #Check if user is done changing cells
    if inp == 'done' or inp == 'DONE':
        break

    #Get list of input
    cell = inp.split(',')

    #Check if the list is empty
    if len(cell) != 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("INVALID FORMAT!")
    else:
        m.getCell(int(cell[0]),int(cell[1])).changeState()
        os.system('cls' if os.name == 'nt' else 'clear')

while 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    m.update()
    m.print()
    inp = input('Next Generation? [yes/no]')
    if inp == 'y' or inp == 'yes':
        continue
    else:
        exit(0)
