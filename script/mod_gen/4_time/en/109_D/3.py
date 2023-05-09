def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 1:
                if w + 1 < W:
                    ans.append((h, w, h, w + 1))
                    A[h][w + 1] += 1
                elif h + 1 < H:
                    ans.append((h, w, h + 1, w))
                    A[h + 1][w] += 1
    print(len(ans))
    for h, w, h1, w1 in ans:
        print(h + 1, w + 1, h1 + 1, w1 + 1)

if __name__ == '__main__':
    main()