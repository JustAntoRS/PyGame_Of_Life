class Cell(object):
    """
    Cell object

    Attributes:
        state (str): state of the Cell, can be 'dead' or 'alive'
    """
    def __init__(self, state = 'dead'):
        """
        Args:
            state (str, optional): state of the Cell, defaults to 'dead'
        """
        self.state = state

    def changeState(self):
        """
        Method that change the state of the cell
        'dead' -> 'alive'
        'alive' -> 'dead'
        """
        if self.state == 'dead':
            self.state = 'alive'
        else:
            self.state = 'dead'
