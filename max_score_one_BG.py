from reachable_BG import reachable
from pop_bubbles_BG import bubbles_popped
from BubbleGraph import BubbleGraph

def max_score_one(bg: BubbleGraph, bubbles): 
    max_score = -1
    bg_final = None
    for bubble in bubbles:
        bg_next, score = optimal_shot(bg, bubble)
        if score > max_score:
            max_score = score
            bg_final = bg_next
    return bg_final, max_score

def optimal_shot(bg: BubbleGraph, bubble: int): 
    max_score = -1
    bg_final = None

    reachables = reachable(bg)
    if len(reachables) == 0:
        return bg, 0

    for pos in reachables:
        bg_new, score = bubbles_popped(bg, pos, bubble)
        if score > max_score:
            max_score = score
            bg_final = bg_new
    return bg_final, max_score


if __name__ == '__main__':
    bg = BubbleGraph.random_graph(5, 5, 5)
    bg.print()
    print('-----')

    final_bg, score = max_score_one(bg, [1, 1, 3, 4])

    final_bg.print()
    print(f'Score: {score}')