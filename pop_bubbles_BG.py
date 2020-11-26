import reachable_BG
from BubbleGraph import BubbleGraph
import numpy as np

def calculate_score(num_balls):
    if num_balls < 3:
        return 0
    elif num_balls == 3:
        return num_balls * 10
    else:
        return (1 + num_balls - 3) * num_balls * 10 / 2 + 30


def adjacent_colors(bg, loc, color):
    # or can pre-store all adjacent entries in a 3D Array
    # ^^ Probably better to prestore adjacencies
    # have to limit adjacencies on the edgess
    return [pos for pos in bg.adjacent(loc) if bg[pos[0]][pos[1]] == color]


def update_matrix(bg, bubs_to_pop, loc, color):
    bg_new = bg.copy()

    if len(bubs_to_pop) >= 3:
        for bubble in bubs_to_pop:
            bg_new[bubble[0]][bubble[1]] = 0
    else:
            bg_new[loc[0]][loc[1]] = color
    
    return bg_new


def bubbles_popped(bg, loc, color, debug=False):
    # do depth first search
    stack = [loc]
    # Use a BubbleGraph for the visited matrix to help formatting
    visited = BubbleGraph(np.zeros((bg.n_rows, bg.n_cols), dtype=int))
    bubs_to_pop = []
    node_count = 0 # keeps track of total nodes
    incrementor = 0

    while len(stack) > 0:
        s = stack.pop()

        if incrementor == 0:
            adj_nodes = adjacent_colors(bg, s, color)

            if debug:
                print(f'Adjacent: {adj_nodes}')
                print(f'Stack: {stack}')
                print(f's: {s}')
                print('Visited:')
                visited.print()
                print('')

        if visited[s[0]][s[1]] == 0:
            visited[s[0]][s[1]] = 1
            bubs_to_pop.append(s)
            node_count += 1
            adj_nodes = adjacent_colors(bg,s,color)

            if debug:
                print(f'Adjacent: {adj_nodes}')
                print(f'Stack: {stack}')
                print(f's: {s}')
                print('Visited:')
                visited.print()
                print('')

            for node in adj_nodes:
                if visited[node[0]][node[1]] == 0:
                    stack.append(node)

        incrementor += 1

    # calculate score
    score = calculate_score(node_count)
    
    # update matrix
    bg_new = update_matrix(bg, bubs_to_pop, loc, color)
    
    if debug:
        return bg_new, score, node_count, visited
    
    return bg_new, score


def test_bubbles_popped(debug=True):
    loc = [1,5]
    color = 1

    bg = BubbleGraph.random_graph(10, 10, 6)

    if debug:
        bg_new, score, n_count, visited = bubbles_popped(bg, loc, color, debug=debug)
        
        print('input')
        bg.print()
        print('output')
        bg_new.print()
        print('visited')
        visited.print()
        print(f'Score: {score}')
        print(f'Bubble Count: {n_count}')
    else:
        bg_new, score = bubbles_popped(bg, loc, color)

        print('input')
        bg.print()
        print('output')
        bg_new.print()
        print(f'Score: {score}')
