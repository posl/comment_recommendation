def main():
    H, W = map(int, input().split())
    A = [[int(a) for a in input().split()] for _ in range(H)]
    ans = []
    for h in range(H):
        for w in range(W):
            if h % 2 == 0:
                if w < W - 1:
                    if A[h][w] % 2 == 1:
                        A[h][w] -= 1
                        A[h][w + 1] += 1
                        ans.append((h + 1, w + 1, h + 1, w + 2))
            else:
                if w > 0:
                    if A[h][w] % 2 == 1:
                        A[h][w] -= 1
                        A[h][w - 1] += 1
                        ans.append((h + 1, w + 1, h + 1, w))
    print(len(ans))
    for a in ans:
        print(*a)
