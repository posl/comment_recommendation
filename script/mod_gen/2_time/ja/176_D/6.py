def main():
    H, W = map(int, input().split())
    CH, CW = map(int, input().split())
    DH, DW = map(int, input().split())
    S = [input() for _ in range(H)]
    CH -= 1
    CW -= 1
    DH -= 1
    DW -= 1
    # 移動A
    def moveA(x, y):
        return [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
    # 移動B
    def moveB(x, y):
        return [(x+i, y+j) for i in range(-2, 3) for j in range(-2, 3)]
    # 移動
    def move(x, y):
        return moveA(x, y) + moveB(x, y)
    # ワープ魔法を使う回数
    warp = [[-1]*W for _ in range(H)]
    warp[CH][CW] = 0
    # 移動回数
    move_count = [[-1]*W for _ in range(H)]
    move_count[CH][CW] = 0
    # 幅優先探索
    queue = [(CH, CW)]
    while queue:
        x, y = queue.pop(0)
        for next_x, next_y in move(x, y):
            if not 0 <= next_x < H or not 0 <= next_y < W:
                continue
            if S[next_x][next_y] == '#':
                continue
            if warp[next_x][next_y] == -1:
                warp[next_x][next_y] = warp[x][y] + 1
                move_count[next_x][next_y] = move_count[x][y] + 1
                queue.append((next_x, next_y))
            elif warp[next_x][next_y] == warp[x][y]:
                if move_count[next_x][next_y] > move_count[x][y] + 1:
                    move_count[next_x][next_y] = move_count[x][y] + 1
                    queue.append((next_x, next_y))
    print(warp[DH][DW])

if __name__ == '__main__':
    main()