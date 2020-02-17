import unittest


def rotateMatrix(matrix):
    """
    Given an image represented by an NxN matrix, where each pixel in the image
    is 4 bytes, write a method to rotate the image by 90 degrees.
    Can you do this inplace?
    """

    n = len(matrix)

    for layer in range(0, n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first

            # backup top
            top = matrix[first][i]

            # Move left to top
            matrix[first][i] = matrix[last - offset][first]

            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]

            # Move top to right
            matrix[i][last] = top

    return matrix


class TestUnit(unittest.TestCase):

    def test_1(self):
        self.assertEqual(rotateMatrix([]), [])
        self.assertEqual(rotateMatrix([1]), [1])

    def test_odd_n(self):
        matrix = [[0, 1, 2, 3],
                  [4, 5, 6, 7],
                  [8, 9, 10, 11],
                  [12, 13, 14, 15]]

        rotated = [[12, 8, 4, 0],
                   [13, 9, 5, 1],
                   [14, 10, 6, 2],
                   [15, 11, 7, 3]]

        self.assertEqual(rotateMatrix(matrix), rotated)

    def test_even_n(self):
        matrix = [[0, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9],
                  [10, 11, 12, 13, 14],
                  [15, 16, 17, 18, 19],
                  [20, 21, 22, 23, 24]]

        rotated = [[20, 15, 10, 5, 0],
                   [21, 16, 11, 6, 1],
                   [22, 17, 12, 7, 2],
                   [23, 18, 13, 8, 3],
                   [24, 19, 14, 9, 4]]

        self.assertEqual(rotateMatrix(matrix), rotated)


if __name__ == '__main__':
    unittest.main()
