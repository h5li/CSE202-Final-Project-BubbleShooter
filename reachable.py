import numpy as np

matrix = [
['.','?','?','?','.'],
['.','?','.','.','.'],
['.','.','r','.','.'],
['r','r','r','r','r'],
['0','0','b','0','0'],
]

matrix = [
['.','.','0','.','.','0','.'],
['.','.','0','0','0','0','.'],
['.','.','.','0','0','0','.'],
['.','.','.','0','.','.','.'],
['r','r','r','r','r','r','r'],
['0','0','0','0','0','0','0'],
['0','0','0','b','0','0','0'],
]

def print_matrix(matrix):
    ret = ""
    for i in range(len(matrix)):
        if i % 2 == 1:
            row_str = " "
        else:
            row_str = ""
        for j in matrix[i]:
            row_str += (str(j) + " ")
        row_str += "\n"
        ret += row_str
    return ret


""" In other words, for a bubble at cell [i, j], it can form groups with bubbles
[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]. Additionally, the diagonal edges
are represented as [i+1, j+1], [i-1, j+1] for odd rows and [i+1, j-1], [i-1, j-1]
for even rows  """
def adjacent(coord, matrix):
    i,j = coord
    assert matrix[i][j] == 0
    if i == 0: # top row
        if j == 0:
            if matrix[i][j+1] != 0 or matrix[i+1][j] != 0:
                return True
        elif j == len(matrix[i]) - 1:
            if matrix[i][j-1] != 0 or matrix[i+1][j] != 0 or matrix[i+1][j-1] != 0:
                return True
        else:
            if matrix[i][j-1] != 0 or matrix[i][j+1] != 0 or \
            matrix[i+1][j-1] != 0 or matrix[i+1][j] != 0:
                return True
    elif i == len(matrix) - 1: # bottom row
        if j == 0:
            if matrix[i][j+1] != 0 or matrix[i-1][j] != 0:
                return True
        elif j == len(matrix[i]) - 1:
            if matrix[i][j-1] != 0 or matrix[i-1][j-1] != 0 or matrix[i-1][j] != 0:
                return True
        else:
            if matrix[i][j-1] != 0 or matrix[i][j+1] != 0 or \
            matrix[i-1][j-1] != 0 or matrix[i-1][j] != 0:
                return True
    elif i % 2 == 1:
        if j == 0:
            if matrix[i-1][j] != 0 or matrix[i-1][j+1] != 0 or \
            matrix[i+1][j] != 0 or matrix[i+1][j+1] != 0 or\
            matrix[i][j+1] != 0:
                return True
        elif j == len(matrix[i]) - 1:
            if matrix[i][j-1] != 0 or matrix[i-1][j] != 0 or matrix[i+1][j] != 0:
                return True
        else:
            if matrix[i][j-1] != 0 or matrix[i][j+1] != 0 or \
            matrix[i+1][j] != 0 or matrix[i+1][j+1] != 0 or \
            matrix[i-1][j] != 0 or matrix[i-1][j+1] != 0:
                return True
    elif i % 2 == 0:
        if j == 0:
            if matrix[i][j+1] != 0 or matrix[i-1][j] != 0 or matrix[i+1][j] != 0:
                return True
        elif j == len(matrix[i]) - 1:
            if matrix[i-1][j] != 0 or matrix[i-1][j-1] != 0 or \
            matrix[i+1][j] != 0 or matrix[i+1][j-1] != 0 or \
            matrix[i][j-1] != 0:
                return True
        else:
            if matrix[i][j-1] != 0 or matrix[i][j+1] != 0 \
            or matrix[i-1][j-1] != 0 or matrix[i-1][j] != 0 \
            or matrix[i+1][j-1] != 0 or matrix[i+1][j] != 0:
                return True
    else:
        raise AssertionError
    return False

def reachable(matrix): # new version, use this one
    ret = set()
    start_col = 0
    if np.sum(matrix) == 0: return ret
    while start_col < len(matrix[0]):
        j = start_col
        for i in range(len(matrix) - 1, -1, -1):
            if i == 0:
                if matrix[i][j] == 0 and adjacent((i,j), matrix):
                        ret.add((i,j))
                    # print("added ", (i,j))
            if matrix[i][j] == 0:
                if adjacent((i,j), matrix):
                    ret.add((i, j))
            else:
                break
                # print("added ", (i,j))
            # print(i,j)
            if i % 2 == 1:
                j += 1
            if j == len(matrix[0]): break
        k = start_col
        for i in range(len(matrix) - 1, -1, -1):
            if i == 0:
                if matrix[i][k] == 0 and adjacent((i,k), matrix):
                        ret.add((i,k))
                    # print("added ", (i,k))
            if matrix[i][k] == 0:
                if adjacent((i,k), matrix):
                    ret.add((i, k))
            else:
                break
                # print("added ", (i,k))
            # print(i,k)
            if i % 2 == 0:
                k -= 1
            if k < 0: break
        start_col += 1
        # print("-"*10)
    return ret

matrix = np.random.randint(1, 2, size=(1, 5))
matrix = np.append(matrix, np.random.randint(0, 2, size=(2, 5)), axis=0)
matrix = np.append(matrix, np.zeros((2,5), dtype=int), axis=0)

# matrix = [[4, 2, 0],[0, 0, 3], [0, 0, 0]]

print(print_matrix(matrix))
# print(np.array(matrix))
reach = reachable(matrix)
for r in reach:
    matrix[r[0]][r[1]] = 9
print(print_matrix(matrix))
print(reachable(matrix))
