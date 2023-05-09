def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    ans = 10**20
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)
