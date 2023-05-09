def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if (i+j) % 2 == 1 and A[i][j] % 2 == 1:
                if j+1 < W:
                    ans.append((i+1, j+1, i+1, j+2))
                    A[i][j+1] += 1
                elif i+1 < H:
                    ans.append((i+1, j+1, i+2, j+1))
                    A[i+1][j] += 1
    for i in range(H):
        for j in range(W-1):
            if A[i][j] % 2 == 1:
                ans.append((i+1, j+1, i+1, j+2))
                A[i][j+1] += 1
    print(len(ans))
    for a in ans:
        print(*a)
