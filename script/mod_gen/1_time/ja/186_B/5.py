def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    #print(H, W)
    #print(A)
    min = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    #print(min)
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min
    print(ans)

if __name__ == '__main__':
    main()