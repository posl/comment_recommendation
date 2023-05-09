def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    N = 0
    ans = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 0:
                continue
            if w + 1 < W:
                A[h][w] -= 1
                A[h][w + 1] += 1
                N += 1
                ans.append([h + 1, w + 1, h + 1, w + 2])
            elif h + 1 < H:
                A[h][w] -= 1
                A[h + 1][w] += 1
                N += 1
                ans.append([h + 1, w + 1, h + 2, w + 1])
    print(N)
    for a in ans:
        print(*a)
