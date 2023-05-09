def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = [[float('inf') for _ in range(W)] for _ in range(H)]
    min_A[0][0] = A[0][0]
    for h in range(H):
        for w in range(W):
            if h > 0:
                min_A[h][w] = min(min_A[h][w], min_A[h-1][w])
            if w > 0:
                min_A[h][w] = min(min_A[h][w], min_A[h][w-1])
            min_A[h][w] = min(min_A[h][w], A[h][w])
    ans = float('inf')
    for h in range(H):
        for w in range(W):
            ans = min(ans, min_A[h][w] + A[h][w] + C * (h + w))
    print(ans)
