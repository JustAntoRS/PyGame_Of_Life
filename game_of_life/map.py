from game_of_life.cell import Cell
import copy

class Map(Cell):
    """
    Class that represents a matrix of n*m Cell
    """
    def __init__(self, num_row, num_column):
        """
        Constructor of Map class that given 2 numbers(num_row, num_column) creates a matrix of Cell objects where
        the cell at position (0,0) of the matrix is the first element and the cell at position
        (num_row - 1, num_column - 1) is the last element of the cell's matrix
        """
        if num_row <= 0 or num_column <= 0:
            raise Exception('Invalid parameters')
        self.num_row = num_row
        self.num_column= num_column
        # Creates a matrix of (num_row * num_column) Cells with dead state
        self.map = [None] * num_row
        for i in range(num_row):
                self.map[i] = [Cell() for j in range(num_column)]


    def getCell(self, pos_row, pos_column):
        """
        Method that return the Cell of the map in the position [pos_row][pos_column]
        or returns None in case there are no Cell at position [pos_row][pos_column]
        """
        if pos_row in range(0, self.num_row) and pos_column in range(0, self.num_column):
            return self.map[pos_row][pos_column]


    def print(self):
        """
        Method that print the map of Cells in a human readable way
        """
        for row in self.map:
            for c in row:
                if c.state == 'dead':
                    print('[ ]', end ='', flush = True)
                else:
                    print('[X]', end ='', flush = True)
            print('')


    def update(self):
        """
        Method that updates the cell's map based on the next rules:
            1.- Every dead cell with 3 alive neighbours is born
            2.- Every alive cell with more than 3 alive neighbours die
            3.- Every alive cell with less than 2 alive neigbours die
        """
        oldMap = copy.deepcopy(self.map)
        for i in range(self.num_row):
            for j in range(self.num_column):
                c = oldMap[i][j]
                neighbours = self.checkNeighbours(i, j)
                if c.state == 'dead' and neighbours[0] == 3:
                    c.changeState()
                elif c.state == 'alive' and (neighbours[0] > 3 or neighbours[0] < 2):
                    c.changeState()
        self.map = copy.deepcopy(oldMap)



    def checkNeighbours(self, pos_row, pos_column):
        """
        Method that given the row and column position of a Cell in the Map
        returns a list with 2 integer elements:
            0th position represents the number of alive neighbours
            1st position represents the number of dead neighbours

         The Cells at the following positions are considered neighbours (if they exist)
         from the cell at position i,j being i the row position and j the column position in the matrix:
            1.- Cell at position i-1,j
            2.- Cell at position i+1,j
            3.- Cell at position i,j+1
            4.- Cell at position i,j-1
            5.- Cell at position i-1,j+1
            6.- Cell at position i-1,j-1
            7.- Cell at position i+1,j+1
            8.- Cell at position i+1,j-1
        """
        neighbours = [0,0] # 0th = number of alive neigbours
                           # 1st = number of dead neigbours
        if self.getCell(pos_row - 1,pos_column): # Up neighbour
            up_n = self.getCell(pos_row - 1, pos_column)
            if up_n.state == 'dead':
                neighbours[1] += 1
            else:
                neighbours[0] += 1

        if self.getCell(pos_row + 1, pos_column): # Down neighbour
            down_n = self.getCell(pos_row + 1, pos_column)
            if down_n.state == 'dead':
                neighbours[1] += 1
            else:
                neighbours[0] += 1

        if self.getCell(pos_row, pos_column + 1): # Rigth neighbour
            rigth_n = self.getCell(pos_row, pos_column + 1)
            if rigth_n.state == 'dead':
                neighbours[1] += 1
            else:
                neighbours[0] += 1

        if self.getCell(pos_row, pos_column - 1): # Left neighbour
            left_n = self.getCell(pos_row, pos_column - 1)
            if left_n.state == 'dead':
                neighbours[1] += 1
            else:
                neighbours[0] += 1

        if self.getCell(pos_row - 1, pos_column + 1): # Up rigth neighbour
            up_rigth_n = self.getCell(pos_row - 1, pos_column + 1)
            if up_rigth_n.state == 'dead':
                neighbours[1] += 1
            else:
                neighbours[0] += 1

        if self.getCell(pos_row - 1, pos_column - 1): # Up left neigbour
            up_left_n = self.getCell(pos_row - 1, pos_column - 1)
            if up_left_n.state == 'dead':
                neighbours[1] += 1
            else:
                neighbours[0] += 1

        if self.getCell(pos_row + 1, pos_column + 1): # Down rigth neighbour
            down_rigth_n = self.getCell(pos_row + 1, pos_column + 1)
            if down_rigth_n.state == 'dead':
                neighbours[1] += 1
            else:
                neighbours[0] += 1

        if self.getCell(pos_row + 1, pos_column - 1): # Down left neighbour
            down_left_n = self.getCell(pos_row + 1, pos_column - 1)
            if down_left_n.state == 'dead':
                neighbours[1] += 1
            else:
                neighbours[0] += 1

        return neighbours
