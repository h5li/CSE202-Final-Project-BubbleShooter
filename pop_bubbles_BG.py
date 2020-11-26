import random
import copy
import reachable_BG
from reachable import print_matrix
from BubbleGraph import BubbleGraph as BG


def calculateScore(numBalls):
    if numBalls < 3:
        return 0
    elif numBalls == 3:
        return numBalls * 10
    else:
        return (1+numBalls-3)*numBalls*10/2 + 30
        
def findAdjacentColors(bg,Loc,Color):
# or can pre-store all adjacent entries in a 3D Array
# ^^ Probably better to prestore adjacencies
# have to limit adjacencies on the edgess
    adj_list = []
    potential_adjacent = bg.adjacent(Loc)
    for i in range(len(potential_adjacent)):
        try:
            if bg[potential_adjacent[i][0]][potential_adjacent[i][1]] == Color:
                adj_list.append(potential_adjacent[i])
        except:
            print('Error: look at node: ',potential_adjacent[i])
            break

    return adj_list


def update_matrix(bg,bubs_to_pop,Loc,Color):
    bg_new = bg.copy()

    if len(bubs_to_pop) >= 3:
        for bubble in bubs_to_pop:
            bg_new[bubble[0]][bubble[1]] = 0
    else:
            bg_new[Loc[0]][Loc[1]] = Color
    
    return bg_new


def bubblesPopped(bg,Loc,Color):

    # do depth first search
    stack  = []
    stack.append(Loc)
    visited =  [[False]*len(bg.matrix[0]) for i in range(len(bg.matrix))] # visited is a dictionary instead of an array
    bubs_to_pop = []
    node_count = 0 # keeps track of total nodes
    incrementor = 0

    while len(stack) > 0:

        s = stack[-1]
        stack.pop()

        if incrementor == 0:
            adj_nodes  = findAdjacentColors(bg,s,Color)
            

        if visited[s[0]][s[1]] == 0:
            visited[s[0]][s[1]] = 1
            bubs_to_pop.append(s)
            node_count +=1
            adj_nodes  = findAdjacentColors(bg,s,Color)
        
            for node in adj_nodes:
                if visited[node[0]][node[1]] == 0:
                    stack.append(node)

        incrementor += 1

    # calculate score
    score = calculateScore(node_count)
    
    # update matrix
    M_new = update_matrix(bg,bubs_to_pop,Loc,Color)
    
    return M_new, score


def bubblesPoppedDebug(bg,Loc,Color):
    
    # do depth first search
    stack  = []
    stack.append(Loc)
    visited =  [[0]*len(bg.matrix[0]) for i in range(len(bg.matrix))] # visited is a dictionary instead of an array
    bubs_to_pop = []
    node_count = 0 # keeps track of total nodes

    incrementor = 0
    while len(stack) > 0:

        
        s = stack[-1]
        stack.pop()
        
        # Adjacent Returns list of adjacent nodes that are same color
        if incrementor == 0:
            adj_nodes  = findAdjacentColors(bg,s,Color)
            print('Adjacent: ',adj_nodes)
            print('Stack: ',stack)
            print('s: ',s)
            print('Visited: \n', print_matrix(visited))

        print('Matrix: \n',print_matrix(bg.matrix))
        

        # print(adjacent)
        if visited[s[0]][s[1]] == 0:
            visited[s[0]][s[1]] = 1
            bubs_to_pop.append(s)
            node_count +=1

            adj_nodes  = findAdjacentColors(bg,s,Color)
            print('Adjacent: ',adj_nodes)
            print('Stack: ',stack)
            print('s: ',s)
            print('Visited:\n',print_matrix(visited))
        
            for node in adj_nodes:
                # print(node)
                if visited[node[0]][node[1]] == 0:
                    stack.append(node)

        incrementor += 1
    # calculate score
    score = calculateScore(node_count)
    
    # update matrix
    M_new = update_matrix(BubGraph.matrix,bubs_to_pop,Loc,Color)
    
    return M_new, score, node_count, visited


def test_bubbles_popped(mode = 'debug'):

    Color = 1
    Loc = [1,5]
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

    bg = BG(copy.deepcopy(test_mat))

    if mode == 'debug':
        M_new,score,n_count,visited= bubblesPoppedDebug(bg,Loc,Color)
        print('input\n')
        print(print_matrix(test_mat))
        print('output\n')
        print(print_matrix(M_new))
        print('visited\n')
        print(print_matrix(visited))
        print('Score: ',score)
        print('Bubble Count: ',n_count)
    else:
        M_new,score= bubblesPopped(bg,Loc,Color)
        print('input\n')
        print(print_matrix(test_mat))
        print('output\n')
        print(print_matrix(M_new))
        print('Score: ',score)

    return



