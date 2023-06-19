def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    B = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            B[i][j] = A[i][j] % 2
    ans = 0
    for i in range(H):
        for j in range(W):
            if B[i][j] == 1:
                if i < H-1:
                    B[i+1][j] += 1
                    ans += 1
                elif j < W-1:
                    B[i][j+1] += 1
                    ans += 1
    print(ans)
main()
