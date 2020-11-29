import numpy as np
from BubbleGraph import BubbleGraph
from reachable_BG import reachable
from pop_bubbles_BG import bubbles_popped

def max_score_many(bg: BubbleGraph, l):
    '''
    l: list of available bubbles
    '''
    if len(l) == 0 or bg.is_empty():
        return [], bg, 0
    
    max_score = -1
    final_bg = None
    final_steps = None

    reachables = reachable(bg)
    if len(reachables) == 0:
        return [], bg, 0

    for pos in reachables:
        bg_next, score = bubbles_popped(bg, pos, l[0])
        steps_rec, bg_rec, score_rec = max_score_many(bg_next, l[1:]) # recursive call
        if score_rec + score > max_score:
            max_score = score_rec + score
            final_bg = bg_rec
            final_steps = [pos] + steps_rec

    return final_steps, final_bg, max_score


def max_score_many_memo(bg: BubbleGraph, l):
    '''
    l: list of available bubbles
    '''

    memo = {}
    def serialize(bg, l):
        serialized = bg.serialize()

        for c in l:
            serialized += str(l) + ' '
    
        return serialized

    def helper(bg, l):
        serialized = serialize(bg, l)
        if serialize(bg, l) in memo:
            return memo[serialized]

        if len(l) == 0 or bg.is_empty():
            return [], bg, 0
        
        max_score = -1
        final_bg = None
        final_steps = None

        reachables = reachable(bg)
        if len(reachables) == 0:
            memo[serialized] = ([], bg, 0)
            return [], bg, 0

        for pos in reachables:
            bg_next, score = bubbles_popped(bg, pos, l[0])
            steps_rec, bg_rec, score_rec = helper(bg_next, l[1:])
            if score_rec + score > max_score:
                max_score = score_rec + score
                final_bg = bg_rec
                final_steps = [pos] + steps_rec

        memo[serialized] = (final_steps, final_bg, max_score)
        return memo[serialized]

    return helper(bg, l)

if __name__ == '__main__':
    bg = BubbleGraph.random_graph(5, 5, 5)
    bg.print()
    l = np.random.randint(1, 6, 5)
    print(l)
    print('-----')

    final_steps, final_bg, score = max_score_many_memo(bg, l)

    print(final_steps)
    final_bg.print()
    print(f'Score: {score}')