from BubbleGraph import BubbleGraph
import numpy as np

def reachable(bg: BubbleGraph, use_memo=False):
    if use_memo:
        memo = np.zeros((bg.n_rows, bg.n_cols), dtype=bool)

    ret = set()

    for col in range(bg.n_cols):
        # Traverse top right
        j = col
        for i in range(bg.n_rows - 1, -1, -1):
            if bg[i][j] == 0:
                if use_memo:
                    if not memo[i][j]:
                        memo[i][j] = True
                        if bg.adjacent((i, j)):
                            ret.add((i, j))
                elif bg.adjacent((i, j)):
                    ret.add((i, j))
            else:
                break

            if i % 2 == 1:
                j += 1
            if j == bg.n_cols:
                break

        # Traverse top left
        k = col
        for i in range(bg.n_rows - 1, -1, -1):
            if bg[i][k] == 0:
                if use_memo:
                    if not memo[i][k]:
                        memo[i][k] = True
                        if bg.adjacent((i, k)):
                            ret.add((i, k))
                elif bg.adjacent((i, k)):
                    ret.add((i, k))
            else:
                break

            if i % 2 == 0:
                k -= 1
            if k < 0:
                break

    return ret


if __name__ == '__main__':
    bg = BubbleGraph.random_graph(5, 5, 2, 2)
    bg.print()

    reach = reachable(bg)
    for r in reach:
        bg[r[0]][r[1]] = 9

    print('----------')
    bg.print()
    print(reach)
