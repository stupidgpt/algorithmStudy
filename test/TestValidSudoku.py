import unittest
from ValidSudoku import Solution

class Test_TestValidSudoku(unittest.TestCase):
    def test_isValidSudoku(self):
        print(Solution().isValidSudoku([[5,3,'.','.',7,'.','.','.','.'],
                                        [6,'.','.',1,9,5,'.','.','.'],
                                        ['.',9,8,'.','.','.','.',6,'.'],
                                        [8,'.','.','.',6,'.','.','.',3],
                                        [4,'.','.',8,'.',3,'.','.',1],
                                        [7,'.','.','.',2,'.','.','.',6],
                                        ['.',6,'.','.','.','.',2,8,'.'],
                                        ['.','.','.',4,1,9,'.','.',5],
                                        ['.','.','.','.',8,'.','.',7,9]]))

if __name__ == '__main__':
    unittest.main()
