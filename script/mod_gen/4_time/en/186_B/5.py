def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(H)]
    minA = min([min(a) for a in A])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)

if __name__ == '__main__':
    main()