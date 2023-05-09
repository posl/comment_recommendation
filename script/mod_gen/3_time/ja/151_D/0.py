def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx * dy != 0:
                        continue
                    if dx == dy == 0:
                        continue
                    x = i + dx
                    y = j + dy
                    if 0 <= x < H and 0 <= y < W:
                        if S[x][y] == "#":
                            ans += 1
    print(ans)

if __name__ == '__main__':
    main()