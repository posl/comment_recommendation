def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_cost = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    min_cost = min(min_cost, A[i][j] + A[k][l] + C * (abs(i-k) + abs(j-l)))
    print(min_cost)
