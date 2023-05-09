def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_cost = 10**18
    for h in range(H):
        for w in range(W):
            if h + 1 < H:
                min_cost = min(min_cost, A[h][w] + A[h + 1][w] + C)
            if w + 1 < W:
                min_cost = min(min_cost, A[h][w] + A[h][w + 1] + C)
            if h - 1 >= 0:
                min_cost = min(min_cost, A[h][w] + A[h - 1][w] + C)
            if w - 1 >= 0:
                min_cost = min(min_cost, A[h][w] + A[h][w - 1] + C)
    print(min_cost)
