import random
import copy

def calculateScore(numBalls):
    if numBalls < 3:
        return 0
    elif numBalls == 3:
        return numBalls * 10
    else:
        return (1+numBalls-3)*numBalls*10/2 + 30
        
def findAdjacentColors(M,Loc,Color):
# or can pre-store all adjacent entries in a 3D Array
# ^^ Probably better to prestore adjacencies
# have to limit adjacencies on the edgess

    adjacent = []
    y = Loc[0]
    x = Loc[1]
    n = len(M[0])
    m = len(M)

    potential_adjacent = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]

    if y % 2 == 1:
        # odd row diagonal
        potential_adjacent.append((y+1, x+1))
        potential_adjacent.append((y-1, x+1))	

    else:
        potential_adjacent.append((y+1, x-1))
        potential_adjacent.append((y-1, x-1))
    
    if x == 0:
        to_delete = []
        for pair in potential_adjacent:
            if pair[1] == -1:
                potential_adjacent.remove(pair)
        
    if x == n-1:
        for pair in potential_adjacent:
            if pair[1] == n:
                potential_adjacent.remove(pair)

    if y == 0:
        for pair in potential_adjacent:
            if pair[0] == -1:
                potential_adjacent.remove(pair)
               
    if y == m-1:
        for pair in potential_adjacent:
            if pair[0] == m:
                potential_adjacent.remove(pair)
               
    for i in range(len(potential_adjacent)):
        try:
            if M[potential_adjacent[i][0]][potential_adjacent[i][1]] == Color:
                adjacent.append(potential_adjacent[i])
        except:
            print('Error: still look at node: ',potential_adjacent[i])
            break

    return adjacent


def update_matrix(M,bubs_to_pop,Loc,Color):

    if len(bubs_to_pop) >= 3:
        for bubble in bubs_to_pop:
            M[bubble[0]][bubble[1]] = 0
    else:
            M[Loc[0]][Loc[1]] = Color
    
    return M

def bubblesPopped(M,Loc,Color):

    # do depth first search
    stack  = []
    stack.append(Loc)
    visited =  [[False]*len(M[0]) for i in range(len(M))] # visited is a dictionary instead of an array
    bubs_to_pop = []
    node_count = 0 # keeps track of total nodes
    while len(stack) > 0:
        s = stack[-1]
        stack.pop()
        # Adjacent Returns list of adjacent nodes that are same 
        # color
        adjacent  = findAdjacentColors(M,s,Color)
        # print(adjacent)
        if visited[s[0]][s[1]] == False:
            visited[s[0]][s[1]] = True
            bubs_to_pop.append(s)
            node_count +=1

        for node in adjacent:
            # print(node)
            if visited[node[0]][node[1]] == False:
                stack.append(node)

    # calculate score
    score = calculateScore(node_count)
    
    # update matrix
    M_new = update_matrix(M,bubs_to_pop,Loc,Color)
    
    return M_new, score


def test_bubbles_popped():

    Color = 1
    Loc = (1,5)
    n_colors = 5
    color_list = [i for i in range(1,n_colors+1)]
    m,n = 10,10
    test_mat = []

    for i in range(m):
        test_mat.append([random.choice(color_list) for i in range(n)])


    for i in range(n):
        test_mat[0][i] = 0
        test_mat[1][i] = 0

    for i in range(2,m):
        test_mat[i][5] = Color

    M = copy.deepcopy(test_mat)

    M_new,score = bubblesPopped(M,Loc,Color)

    return test_mat,M_new,score
