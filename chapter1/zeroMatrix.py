import unittest


def zeroMatrix(matrix):
    """
    Write an algorithm so that if an element in an MxN matrix is 0,
    its entire row and column are set to 0
    """

    '''
    Solution: Use the first row and first column as bitmaps of rows and columns with 0
    eg: if matrix[0][i] is set to 0 then a zero exists in row 0 hence row 0 needs to be
    zeroed. Similar to column.
    However, since we're reusing the first row and column, we need to first check if they
    have any zero in them before we overwrite the values.
    '''

    # Check if the first row and first column have any zeroes
    rows = len(matrix)

    if rows <= 1:
        return matrix

    firstRowHasZero = 0
    firstColHasZero = 0
    columns = len(matrix[0])
    for col in range(columns):
        if matrix[0][col] == 0:
            firstRowHasZero = 1
            break

    for row in range(rows):
        if matrix[row][0] == 0:
            firstColHasZero = 1
            break

    # Iterate through the rest of matrix
    for row in range(1, rows):
        for col in range(1, columns):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    # Now zero out all rows with a zero
    for col in range(1, columns):
        if matrix[0][col] == 0:
            _zeroOutColumn(matrix, col)

    # then the columns
    for row in range(1, rows):
        if matrix[row][0] == 0:
            _zeroOutRow(matrix, row)

    # Now zero out the first row and column if necessary
    if firstRowHasZero:
        _zeroOutRow(matrix, 0)

    if firstColHasZero:
        _zeroOutColumn(matrix, 0)

    return matrix


def _zeroOutRow(matrix, row):
    for col in range(0, len(matrix[0])):
        matrix[row][col] = 0


def _zeroOutColumn(matrix, col):
    for row in range(0, len(matrix)):
        matrix[row][col] = 0


class TestUnit(unittest.TestCase):

    def test_1(self):
        self.assertEqual(zeroMatrix([]), [])
        self.assertEqual(zeroMatrix([[1]]), [[1]])
        self.assertEqual(zeroMatrix([[0]]), [[0]])
        self.assertEqual(zeroMatrix([[1, 1],
                                     [1, 0]]),
                         [[1, 0],
                          [0, 0]])

    def test_2(self):
        matrix = [[1, 1, 1, 0, 1],
                  [0, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1],
                  [1, 0, 1, 1, 1]]

        zeroed = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0]]

        self.assertEqual(zeroMatrix(matrix), zeroed)


if __name__ == '__main__':
    unittest.main()
