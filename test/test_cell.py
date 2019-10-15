import unittest
from game_of_life.cell import *

class CellTestCases(unittest.TestCase):
    def setUp(self):
        self.c = Cell();

    def test_default_state(self):
        self.assertEqual('dead', self.c.state, 'Wrong cell initilization, expected dead state' )

    def test_change_state(self):
        self.c.changeState()
        self.assertEqual('alive', self.c.state, 'Wrong state after changeState() call, expected alive state' )

    def test_change_state_x2(self):
        self.c.changeState()
        self.c.changeState()
        self.assertEqual('dead', self.c.state, 'Wron state afer 2 changeState() calls, expected dead state' )


def CellSuite():
    cellSuite = unittest.TestSuite()
    cellSuite.addTest(CellTestCases('test_default_state'))
    cellSuite.addTest(CellTestCases('test_change_state'))
    cellSuite.addTest(CellTestCases('test_change_state_x2'))
    return cellSuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(CellSuite())
