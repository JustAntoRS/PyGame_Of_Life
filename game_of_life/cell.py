class Cell(object):
    def __init__(self, state = 'dead'):
        self.state = state

    def changeState(self):
        if self.state == 'dead':
            self.state = 'alive'
        else:
            self.state = 'dead'
