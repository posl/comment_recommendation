def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                ans += 1
    if ans == 1:
        ans = 2
    print(ans)
