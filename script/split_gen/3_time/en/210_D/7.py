def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_cost = [min(a) for a in A]
    min_cost = [min(min_cost)] * W
    for i in range(H):
        for j in range(W):
            min_cost[j] = min(min_cost[j], A[i][j])
            if A[i][j] + min_cost[j] - C < 0:
                print(A[i][j] + min_cost[j])
                return
    print(min_cost[0] + C)
