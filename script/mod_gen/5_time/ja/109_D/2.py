def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W-1:
                    ans.append([i+1, j+1, i+1, j+2])
                    A[i][j+1] += 1
                else:
                    if i < H-1:
                        ans.append([i+1, j+1, i+2, j+1])
                        A[i+1][j] += 1
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

if __name__ == '__main__':
    main()