def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i != k or j != l:
                        ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)

if __name__ == '__main__':
    main()