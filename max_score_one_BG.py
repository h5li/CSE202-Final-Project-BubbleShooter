from reachable_BG import reachable
from pop_bubbles_BG import bubblesPopped
from BubbleGraph import BubbleGraph

def optimal_shot(bg: BubbleGraph, bubbles): 
    max_score = 0
    for bubble in bubbles:
        max_score = max(max_score, max_score_one(bg, bubble))
    return max_score

def max_score_one(bg: BubbleGraph, bubble: int): 
    available_positions = reachable(bg) 
    max_score = 0
    bg_final = None
    for pos in available_positions:
        bg_new, score = bubblesPopped(bg, pos, bubble)
        if score > max_score:
            max_score = score
            bg_final = bg_new
    return bg_final, max_score
