def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10 ** 18
    for i in range(H):
        for j in range(W):
            for a in range(H):
                for b in range(W):
                    if i == a and j == b:
                        continue
                    ans = min(ans, A[i][j] + A[a][b] + C * (abs(i - a) + abs(j - b)))
    print(ans)
