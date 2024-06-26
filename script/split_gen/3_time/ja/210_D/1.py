def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)
