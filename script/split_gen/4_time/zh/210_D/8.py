def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_cost = float('inf')
    for i in range(H):
        for j in range(W):
            for k in range(i, H):
                for l in range(j, W):
                    if i == k and j == l:
                        continue
                    cost = A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l))
                    min_cost = min(min_cost, cost)
    print(min_cost)
