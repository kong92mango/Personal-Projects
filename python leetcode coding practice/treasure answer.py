def Find_Treasure(checkboard, src, dst):
    visited = set()
    Best_path = {}
    Best_path['path'] = []
    Best_path['len'] = [len(checkboard) * len(checkboard[0]) + 1]
    Path = []

    global cur_treasure
    cur_treasure = 0
    total_treasure = 0

    for i in xrange(len(checkboard)):
        for j in xrange(len(checkboard[0])):
            if checkboard[i][j] == 1:
                total_treasure += 1

    def DFS(src):
        global cur_treasure
        if len(Path) + 1 >= Best_path['len']: #
            return
        else:
            # forward pass
            Path.append(src)
            visited.add(src)
            if checkboard[src[0]][src[1]] == 1:
                cur_treasure += 1
            if src == dst:
                if cur_treasure == total_treasure:
                        Best_path['len'] = len(Path)
                        Best_path['path'] = Path[:]
                return

            for step in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x, y = src[0] + step[0], src[1] + step[1]
                if 0 <= x < len(checkboard) and 0 <= y < len(checkboard[0]) and checkboard[x][y] >= 0 and (x, y) not in visited:
                    DFS((x, y))

            # backward pass
            if checkboard[src[0]][src[1]] == 1:
                cur_treasure -= 1
            visited.remove(src)
            Path.pop()

    DFS(src)
    return Best_path
