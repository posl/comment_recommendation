def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 1:
                if h == H-1 and w == W-1:
                    continue
                elif w == W-1:
                    ans.append([h+1, w+1, h+2, w+1])
                    A[h+1][w] += 1
                else:
                    ans.append([h+1, w+1, h+1, w+2])
                    A[h][w+1] += 1
    print(len(ans))
    for a in ans:
        print(*a)
