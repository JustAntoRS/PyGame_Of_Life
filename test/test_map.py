import unittest
from game_of_life.map import *

class MapInitTestCases(unittest.TestCase):
    def test_init_not_valid_0(self):
        with self.assertRaises(Exception):
            Map(0,0)

    def test_init_not_valid_1(self):
        with self.assertRaises(Exception):
            Map(-1,0)

    def test_init_not_valid_2(self):
        with self.assertRaises(Exception):
            Map(0,-1)

    def test_init_not_valid_3(self):
        with self.assertRaises(Exception):
            Map(-1,-1)

    def test_init_not_valid_4(self):
        with self.assertRaises(Exception):
            Map(1,0)

    def test_init_not_valid_5(self):
        with self.assertRaises(Exception):
            Map(0,1)

    @unittest.expectedFailure
    def test_init_valid(self):
        with self.assertRaises(Exception):
            Map(1,1)

class MapChangeStateTestCases(unittest.TestCase):
    def setUp(self):
        self.map_5_5 = Map(5, 5)

    def test_not_valid_0(self):
        with self.assertRaises(ValueError):
            self.map_5_5.changeCellState(5,5)

    def test_not_valid_1(self):
        with self.assertRaises(ValueError):
            self.map_5_5.changeCellState(-1,3)

    def test_not_valid_2(self):
        with self.assertRaises(ValueError):
            self.map_5_5.changeCellState(3, -1)

    def test_valid_0(self):
        self.map_5_5.changeCellState(0, 0)
        self.assertEqual(1, self.map_5_5._map[0][0])

    def test_valid_1(self):
        self.map_5_5.changeCellState(0, 0)
        self.map_5_5.changeCellState(0, 0)
        self.assertEqual(0, self.map_5_5._map[0][0])

class MapGetCellTestCases(unittest.TestCase):
    def setUp(self):
        self.map_5_5 = Map(5, 5)

    def test_not_valid_0(self):
        self.assertEqual(None, self.map_5_5.getCellState(-1, 0))

    def test_not_valid_1(self):
        self.assertEqual(None, self.map_5_5.getCellState(0, -1))

    def test_not_valid_2(self):
        self.assertEqual(None, self.map_5_5.getCellState(-1, -1))

    def test_not_valid_3(self):
        self.assertEqual(None, self.map_5_5.getCellState(1, 5))

    def test_not_valid_4(self):
        self.assertEqual(None, self.map_5_5.getCellState(5, 1))

    def test_not_valid_5(self):
        self.assertEqual(None, self.map_5_5.getCellState(5, 5))

    def test_valid_0(self):
        self.assertEqual('dead', self.map_5_5.getCellState(0,0))

    def test_valid_1(self):
        self.map_5_5.changeCellState(4,4)
        self.assertEqual('alive', self.map_5_5.getCellState(4,4))


class MapCheckNeighboursTestCases(unittest.TestCase):
    def setUp(self):
        self.map10_10 = Map(10,10)


    def test_0(self):
        self.assertEqual(0,self.map10_10.checkNeighbours(1,1))


    def test_1(self):
        self.map10_10.changeCellState(0,0)
        self.map10_10.changeCellState(0,1)
        self.map10_10.changeCellState(0,2)
        self.map10_10.changeCellState(1,0)
        self.map10_10.changeCellState(1,2)
        self.map10_10.changeCellState(2,0)
        self.map10_10.changeCellState(2,1)
        self.map10_10.changeCellState(2,2)
        self.assertEqual(8,self.map10_10.checkNeighbours(1,1))


    def test_2(self):
        self.map10_10.changeCellState(0,1)
        self.assertEqual(1,self.map10_10.checkNeighbours(0,0))


    def test_3(self):
        self.map10_10.changeCellState(0,0)
        self.assertEqual(1,self.map10_10.checkNeighbours(0,1))


class MapUpdateTestCases(unittest.TestCase):
    def setUp(self):
        self.map10_10 = Map(10,10)

    def test_0(self):
        self.map10_10.changeCellState(5,5)
        self.map10_10.changeCellState(5,6)
        self.map10_10.changeCellState(6,6)
        self.map10_10.changeCellState(6,7)
        self.map10_10.changeCellState(7,6)
        self.map10_10.update()
        self.assertEqual('alive',self.map10_10.getCellState(5,5))
        self.assertEqual('alive',self.map10_10.getCellState(5,6))
        self.assertEqual('alive',self.map10_10.getCellState(5,7))
        self.assertEqual('alive',self.map10_10.getCellState(6,7))
        self.assertEqual('alive',self.map10_10.getCellState(7,6))
        self.assertEqual('alive',self.map10_10.getCellState(7,7))

def MapSuite():
    mapSuite = unittest.TestSuite()
    #Init test cases
    for i in range(0, 6):
        mapSuite.addTest(MapInitTestCases('test_init_not_valid_' + str(i)))
    mapSuite.addTest(MapInitTestCases('test_init_valid'))

    #Change State test cases
    for i in range(0,3):
        mapSuite.addTest(MapChangeStateTestCases('test_not_valid_' + str(i)))
        if(i < 2):
            mapSuite.addTest(MapChangeStateTestCases('test_valid_' + str(i)))

    #Get State test cases
    for i in range(0,6):
        mapSuite.addTest(MapGetCellTestCases('test_not_valid_' + str(i)))
        if i < 2:
            mapSuite.addTest(MapGetCellTestCases('test_valid_' + str(i)))

    #Check neighbours test cases
    for i in range(0,4):
        mapSuite.addTest(MapCheckNeighboursTestCases('test_' + str(i)))

    #Update test cases
    mapSuite.addTest(MapUpdateTestCases('test_0'))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(MapSuite())
