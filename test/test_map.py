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

class MapGetCellTestCases(unittest.TestCase):
    def setUp(self):
        self.map_1_1 = Map(1,1)
        self.map_5_5 = Map(5,5)

    def test_not_valid_0(self):
        self.assertEqual(None, self.map_1_1.getCell(-1, 0))

    def test_not_valid_1(self):
        self.assertEqual(None, self.map_1_1.getCell(0, -1))

    def test_not_valid_2(self):
        self.assertEqual(None, self.map_1_1.getCell(-1, -1))

    def test_not_valid_3(self):
        self.assertEqual(None, self.map_1_1.getCell(1, 3))

    def test_not_valid_4(self):
        self.assertEqual(None, self.map_1_1.getCell(3, 1))

    def test_not_valid_5(self):
        self.assertEqual(None, self.map_1_1.getCell(3, 3))

    def test_valid_0(self):
        self.assertEqual(self.map_1_1.map[0][0], self.map_1_1.getCell(0,0))

    def test_valid_1(self):
        self.assertEqual(self.map_5_5.map[4][4], self.map_5_5.getCell(4,4))

class MapCheckNeighboursTestCases(unittest.TestCase):
    def setUp(self):
        self.map10_10 = Map(10,10)


    def test_0(self):
        self.assertEqual(0,self.map10_10.checkNeighbours(1,1)[0])
        self.assertEqual(8,self.map10_10.checkNeighbours(1,1)[1])


    def test_1(self):
        self.map10_10.getCell(0,0).changeState()
        self.map10_10.getCell(0,1).changeState()
        self.map10_10.getCell(0,2).changeState()
        self.map10_10.getCell(1,0).changeState()
        self.map10_10.getCell(1,2).changeState()
        self.map10_10.getCell(2,0).changeState()
        self.map10_10.getCell(2,1).changeState()
        self.map10_10.getCell(2,2).changeState()
        self.assertEqual(8,self.map10_10.checkNeighbours(1,1)[0])
        self.assertEqual(0,self.map10_10.checkNeighbours(1,1)[1])


    def test_2(self):
        self.map10_10.getCell(0,1).changeState()
        self.assertEqual(1,self.map10_10.checkNeighbours(0,0)[0])
        self.assertEqual(2,self.map10_10.checkNeighbours(0,0)[1])


    def test_3(self):
        self.map10_10.getCell(0,0).changeState()
        self.assertEqual(1,self.map10_10.checkNeighbours(0,1)[0])
        self.assertEqual(4,self.map10_10.checkNeighbours(0,1)[1])


class MapUpdateTestCases(unittest.TestCase):
    def setUp(self):
        self.map10_10 = Map(10,10)
        self.map20_20 = Map(20,20)

    def test_1(self):
        self.map10_10.getCell(5,5).changeState()
        self.map10_10.getCell(5,6).changeState()
        self.map10_10.getCell(6,6).changeState()
        self.map10_10.getCell(6,7).changeState()
        self.map10_10.getCell(7,6).changeState()
        self.map10_10.update()
        self.assertEqual('alive',self.map10_10.getCell(5,5).state)
        self.assertEqual('alive',self.map10_10.getCell(5,6).state)
        self.assertEqual('alive',self.map10_10.getCell(5,7).state)
        self.assertEqual('alive',self.map10_10.getCell(6,7).state)
        self.assertEqual('alive',self.map10_10.getCell(7,7).state)
        self.assertEqual('alive',self.map10_10.getCell(7,6).state)

def MapSuite():
    mapSuite = unittest.TestSuite()
    mapSuite.addTest(MapInitTestCases('test_init_valid'))
    for i in range(0,6):
        mapSuite.addTest(MapInitTestCases('test_init_not_valid_' + str(i)))
        mapSuite.addTest(MapGetCellTestCases('test_not_valid_' + str(i)))
        if i in range(0,2):
            mapSuite.addTest(MapGetCellTestCases('test_valid_' + str(i)))
        if i in range(0,4):
            mapSuite.addTest(MapCheckNeighboursTestCases('test_' + str(i)))
    mapSuite.addTest(MapUpdateTestCases('test_1'))
    return mapSuite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(MapSuite())
