def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    count = 0
    # 上下左右の方向を表すベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        x = X - 1
        y = Y - 1
        while True:
            x += dx[i]
            y += dy[i]
            if 0 <= x < H and 0 <= y < W and S[x][y] == '.':
                count += 1
            else:
                break
    print(count + 1)
