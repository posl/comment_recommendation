def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    # 0:U, 1:D, 2:L, 3:R
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    d = [0, 1, 2, 3]
    # 0:U, 1:D, 2:L, 3:R
    d2c = ['U', 'D', 'L', 'R']
    # 0:U, 1:D, 2:L, 3:R
    d2i = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    x, y = 0, 0
    while True:
        c = grid[y][x]
        i = d2i[c]
        x += dx[i]
        y += dy[i]
        # 範囲外に出たら終了
        if x < 0 or x >= w or y < 0 or y >= h:
            break
        # 始点に戻ったら無限ループ
        if x == 0 and y == 0:
            print(-1)
            return
    print(y + 1, x + 1)
