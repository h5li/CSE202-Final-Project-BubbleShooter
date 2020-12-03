import numpy as np

class BubbleGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])

    @staticmethod
    def random_graph(n_rows: int, n_cols: int, n_colors: int, n_empty: int):
        '''
        Generates a random bubble graph.
        '''
        matrix = np.random.randint(1, n_colors + 1, (n_rows - n_empty, n_cols))
        matrix = np.concatenate((matrix, np.zeros((n_empty, n_cols), dtype=int)), axis=0)
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
        for i in range(len(self.matrix)):
            row_str = ''
            if i % 2 == 1: # Add skew
                row_str += ' '

            for color in self.matrix[i]:
                row_str += str(color) + ' '

            print(row_str)

    def __getitem__(self, key):
        '''
        use bg[i] to get the i'th row of the matrix, instead of bg.matrix[i].
        '''
        return self.matrix[key]

    def adjacent(self, pos):
        '''
        Outputs a list of positions that are adjacent to the given position. All the positions will be filled (non-zero).
        '''
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        diagonals_odd = [[1, 1], [-1, 1]]
        diagonals_even = [[1, -1], [-1, -1]]

        if pos[0] % 2 == 1:
            directions += diagonals_odd
        else:
            directions += diagonals_even

        adj = []

        for d in directions:
            x = pos[0] + d[0]
            y = pos[1] + d[1]
            if x >= 0 and x < len(self.matrix) and y >= 0 and y < len(self.matrix[x]) and self.matrix[x][y] != 0:
                adj.append([x, y])
        
        return adj

    def is_empty(self):
        for row in self.matrix:
            for bubble in row:
                if bubble != 0:
                    return False
        
        return True

    def copy(self):
        '''
        Returns a deep copy of the original bubble graph.
        '''
        return BubbleGraph(np.array(self.matrix))