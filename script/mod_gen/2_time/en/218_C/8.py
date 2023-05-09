def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(n)]
    # Tの左上の#の位置を求める
    t_y, t_x = -1, -1
    for i in range(n):
        for j in range(n):
            if t[i][j] == "#":
                t_y, t_x = i, j
                break
        if t_y != -1:
            break
    # Sの#の位置を求める
    s_yx = []
    for i in range(n):
        for j in range(n):
            if s[i][j] == "#":
                s_yx.append((i, j))
    # Sの#をTの左上の#に合わせる
    for sy, sx in s_yx:
        if sy - t_y >= n or sx - t_x >= n or sy - t_y < 0 or sx - t_x < 0:
            print("No")
            exit()
        if t[sy - t_y][sx - t_x] != "#":
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()