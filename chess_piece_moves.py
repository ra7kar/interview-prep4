# given a chess piece find the valid moves.

#TDD approach, (Test Driven approach)

# standard
from signal import raise_signal
import unittest
from abc import ABC, abstractmethod


# External
from numpy.testing._private.parameterized import parameterized


class ChessPieces(ABC):
    def __init__(self, row, col) -> None:
        # check inputs
        if row > 8 or row < 1:
            raise ValueError('row out of bounds, {row}')
        if col > 8 or col < 1:
            raise ValueError('col is out of bounds, {col}')

        self.row = row
        self.col = col

    def get_position(self):
        return (self.row, self.col)

    @abstractmethod
    def get_valid_moves(self):
        raise NotImplemented

    @property
    def name(self):
        return type(self).__name__

def is_position_valid(row, col):
    if row > 8 or row < 1:
        return False
    if col > 8 or col < 1:
        return False
    return True

class Queen(ChessPieces):

    def get_valid_moves(self):

        row, col = self.get_position()
        valid_moves = [ ]

        for r_shift in [-1, 0, 1]:
            for c_shift in [-1, 0, 1]:
                if r_shift == 0 and c_shift == 0:
                    continue
                new_row, new_col = row, col

                while is_position_valid(new_row, new_col):
                    if new_row != row or new_col != col:
                        valid_moves.append((new_row, new_col))

                    new_row += r_shift
                    new_col += c_shift
        
        return valid_moves

    def get_move_count(self):
        return len(self.get_valid_moves())


class TestChessPieces(unittest.TestCase):
    @parameterized.expand([
        ((4,4), 27),
        ((3,5), 25),
        ((6,5), 25),
        ((1,7), 21),
    ])

    def test_pieces(self, input, result):
        queen = Queen(input[0], input[1])
        self.assertEqual(queen.get_move_count(), result)



if __name__ == "__main__":
    unittest.main()
