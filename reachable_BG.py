from BubbleGraph import BubbleGraph

def reachable(bg: BubbleGraph):
    ret = set()

    for col in range(bg.n_cols):
        # Traverse top right
        j = col
        for i in range(bg.n_rows - 1, -1, -1):
            if bg[i][j] == 0:
                if bg.adjacent((i, j)):
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
                if bg.adjacent((i, k)):
                    ret.add((i, k))
            else:
                break

            if i % 2 == 0:
                k -= 1
            if k < 0: 
                break

    return ret


if __name__ == '__main__':
    bg = BubbleGraph.random_graph(5, 5, 3)
    bg.print()

    reach = reachable(bg)
    for r in reach:
        bg[r[0]][r[1]] = 9

    print('----------')
    bg.print()
    print(reach)
