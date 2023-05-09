def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for w in range(W):
        for h in range(H):
            print(A[h][w], end=' ')
        print()
