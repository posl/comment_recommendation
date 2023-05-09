def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    count = [[0] * W for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                continue
            for x in range(w + 1, W):
                if S[h][x] == '#':
                    break
                count[h][x] += 1
            for x in range(w - 1, -1, -1):
                if S[h][x] == '#':
                    break
                count[h][x] += 1
            for y in range(h + 1, H):
                if S[y][w] == '#':
                    break
                count[y][w] += 1
            for y in range(h - 1, -1, -1):
                if S[y][w] == '#':
                    break
                count[y][w] += 1
    for h in range(H):
        for w in range(W):
            ans = max(ans, count[h][w])
    print(ans + 1)

if __name__ == '__main__':
    main()