import numpy as np

class BubbleGraph:
    def __init__(self, matrix):
        self.matrix = matrix

    @staticmethod
    def random_graph(n_rows: int, n_cols: int, n_colors: int):
        '''
        Generates a random bubble graph.
        '''
        matrix = np.random.randint(0, n_colors + 1, (n_rows, n_cols))
        return BubbleGraph(matrix)

    def serialize(self):
        '''
        Serialize as a string, to be used as a key in memoization.
        '''
        serialized = ''
        for row in self.matrix:
            for color in row:
                serialized += str(color) + ' '

        return serialized
    
    def print(self):
        '''
        Prints the matrix in a user-friendly manner.
        '''
        for row in self.matrix:
            row_str = ''
            for color in row:
                row_str += str(color) + ' '

            print(row_str)

    def __getitem__(self, key):
        '''
        use bg[i] to get the i'th row of the matrix, instead of bg.matrix[i].
        '''
        return self.matrix[key]