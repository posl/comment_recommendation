def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            cnt = 0
            for di, dj in ((0, 0), (0, 1), (1, 0), (1, 1)):
                if S[i+di][j+dj] == '#':
                    cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)
