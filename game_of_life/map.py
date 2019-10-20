import copy

class Map():
    """
    Class that represents a matrix of n*m Cells
    """
    def __init__(self, num_row, num_column):
        """
        Args:
            num_row (int): The number of rows of the matrix
            num_column (int): The number of columns of the matrix
        Raises:
            ValueError: if num_row or num_column are less than or equal to 0
        """
        #Exception handling
        if num_row <= 0:
            raise ValueError('num_row is {} and should be greater than 0'.format(num_row))
        if num_column <= 0:
            raise ValueError('num_column is {} and should be greater than 0'.format(num_column))

        self._num_row = num_row
        self._num_column= num_column
        # Creates a matrix of (num_row * num_column) int numbers:
        #   0 -> the cell state is dead
        #   1 -> the cell state is alive
        self._map = [None] * num_row
        for i in range(num_row):
                self._map[i] = [0 for j in range(num_column)]


    def getCellState(self, pos_row, pos_column):
        """
        Args:
            pos_row (int): represents the row where the desired Cell is
            pos_columnn (int): represetns the column where the desired Cell is

        Returns:
            str: If the cell exist return state of the cell at the given position
                ('dead' or 'alive'), otherwise returns None
        """
        if pos_row in range(0, self._num_row) and pos_column in range(0, self._num_column):
            c = self._map[pos_row][pos_column]
            if c == 0:
                return 'dead'
            else:
                return 'alive'

    def print(self):
        """
        Method that print the map of Cells in a human readable way:
        [ ] -> means the cell state is: dead
        [X] -> means the cell state is: alive
        """
        for row in self._map:
            for c in row:
                if c == 0:
                    print('[ ]', end ='', flush = True)
                else:
                    print('[X]', end ='', flush = True)
            print('')


    def changeCellState(self, pos_row, pos_column):
        """
        Args:
            pos_row (int): row position of the desired cell
            pos_column (int): column position of the desired cell

        Returns:
            None: change the state of the cell, given it's position, on the matrix

        Raises:
            ValueError: if there's no Cell at position (pos_row, pos_column)
        """
        if pos_row in range(0,self._num_row) and pos_column in range(0,self._num_column):
            if self._map[pos_row][pos_column] == 0:
                self._map[pos_row][pos_column] = 1
            else:
                self._map[pos_row][pos_column] = 0
        else:
            raise ValueError('Cell at position ({},{}) does not exist'.format(pos_row, pos_column))


    def checkNeighbours(self, pos_row, pos_column):
        """
        Args:
            pos_row (int): row position of the desired cell
            pos_column (int): column position of the desired cell

        Returns:
            int: The number of neighbouring cells that are alive

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
        neighbours = 0

        # Up neighbour
        up_n = self.getCellState(pos_row - 1, pos_column)
        if up_n == 'alive':
            neighbours += 1

        # Down neighbour
        down_n = self.getCellState(pos_row + 1, pos_column)
        if down_n == 'alive':
            neighbours += 1

        # Rigth neigbour
        rigth_n = self.getCellState(pos_row, pos_column + 1)
        if rigth_n == 'alive':
            neighbours += 1

        # Left neighbour
        left_n = self.getCellState(pos_row, pos_column - 1)
        if left_n == 'alive':
            neighbours += 1

        # Up-rigth neigbour
        up_rigth_n = self.getCellState(pos_row - 1, pos_column + 1)
        if up_rigth_n == 'alive':
            neighbours += 1

        # Up-left neigbour
        up_left_n = self.getCellState(pos_row - 1, pos_column - 1)
        if up_left_n == 'alive':
            neighbours += 1

        # Down-rigth neigbour
        down_rigth_n = self.getCellState(pos_row + 1, pos_column + 1)
        if down_rigth_n == 'alive':
            neighbours += 1

        # Down-left neigbour
        down_left_n = self.getCellState(pos_row + 1, pos_column - 1)
        if down_left_n == 'alive':
            neighbours += 1

        return neighbours

    def update(self):
        """
        Method that updates the Cell's matrix based on the next rules:
            1.- Every dead cell with 3 alive neighbours is born
            2.- Every alive cell with more than 3 alive neighbours die
            3.- Every alive cell with less than 2 alive neigbours die
        """

        toChangeCells = [] # List to store the position of the cells to change their state

        # Check which cells should change
        for i in range(self._num_row):
            for j in range(self._num_column):
                c = self.getCellState(i, j)
                neighbours = self.checkNeighbours(i, j)
                if c == 'dead' and neighbours == 3:
                    toChangeCells.append((i, j))
                elif c == 'alive' and (neighbours > 3 or neighbours < 2):
                    toChangeCells.append((i, j))

        # Change cells state
        for pos in toChangeCells:
            self.changeCellState(pos[0], pos[1])
