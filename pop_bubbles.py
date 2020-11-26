import random
import copy
import sys
sys.path.append('G:\My Drive\CLASSES\FA20\CSE 202\Project\CSE202-Final-Project-BubbleShooter')
import reachable


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
        oob_indices = []
        for i,pair in enumerate(potential_adjacent):
            if pair[1] == -1:
                oob_indices.extend([i])
        potential_adjacent = [ind for i, ind in enumerate(potential_adjacent) \
                              if i not in oob_indices]           
    
               
    if x == n-1:
        oob_indices = []
        for i,pair in enumerate(potential_adjacent):
            if pair[1] == n:
                oob_indices.extend([i])
        potential_adjacent = [ind for i, ind in enumerate(potential_adjacent) \
                              if i not in oob_indices] 

    if y == 0:
        oob_indices = []
        for i,pair in enumerate(potential_adjacent):
            if pair[0] == -1:
                oob_indices.extend([i])
        potential_adjacent = [ind for i, ind in enumerate(potential_adjacent) \
                              if i not in oob_indices] 
               
    if y == m-1:
        oob_indices = []
        for i,pair in enumerate(potential_adjacent):
            if pair[0] == m:
                oob_indices.extend([i])
        potential_adjacent = [ind for i, ind in enumerate(potential_adjacent) \
                              if i not in oob_indices] 
               
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
        # Adjacent Returns list of adjacent nodes that are same color
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


def bubblesPoppedDebug(M,Loc,Color):
    
    # do depth first search
    stack  = []
    stack.append(Loc)
    visited =  [[0]*len(M[0]) for i in range(len(M))] # visited is a dictionary instead of an array
    bubs_to_pop = []
    node_count = 0 # keeps track of total nodes

    incrementor = 0
    while len(stack) > 0:

        
        s = stack[-1]
        stack.pop()
        

        # Adjacent Returns list of adjacent nodes that are same color
        if incrementor == 0:
            adjacent  = findAdjacentColors(M,s,Color)
            # print('Adjacent: ',adjacent)
            # print('Stack: ',stack)
            # print('s: ',s)
            # print('Visited: \n', reachable.print_matrix(visited))
        

        # print('Matrix: \n',reachable.print_matrix(M))
        

        # print(adjacent)
        if visited[s[0]][s[1]] == 0:
            visited[s[0]][s[1]] = 1
            bubs_to_pop.append(s)
            node_count +=1

            adjacent  = findAdjacentColors(M,s,Color)
            # print('Adjacent: ',adjacent)
            # print('Stack: ',stack)
            # print('s: ',s)
            # print('Visited:\n',reachable.print_matrix(visited))
        
            for node in adjacent:
                # print(node)
                if visited[node[0]][node[1]] == 0:
                    stack.append(node)

        incrementor += 1
    # calculate score
    score = calculateScore(node_count)
    
    # update matrix
    M_new = update_matrix(M,bubs_to_pop,Loc,Color)
    
    return M_new, score, node_count, visited


def test_bubbles_popped(mode = 'debug'):

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
        test_mat[6][i] = 1

    for i in range(2,m):
        test_mat[i][5] = Color

    M = copy.deepcopy(test_mat)

    if mode == 'debug':
        M_new,score,n_count,visited= bubblesPoppedDebug(M,Loc,Color)
        print('input\n')
        print(reachable.print_matrix(test_mat))
        print('output\n')
        print(reachable.print_matrix(M_new))
        print('visited\n')
        print(reachable.print_matrix(visited))
        print('Score: ',score)
        print('Bubble Count: ',n_count)
    else:
        M_new,score= bubblesPopped(M,Loc,Color)
        print('input\n')
        print(reachable.print_matrix(test_mat))
        print('output\n')
        print(reachable.print_matrix(M_new))
        print('Score: ',score)

    return
