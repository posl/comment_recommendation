def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    #print(A)
    minA = min([min(a) for a in A])
    #print(minA)
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)

if __name__ == '__main__':
    main()