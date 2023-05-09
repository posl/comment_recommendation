def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    ans = 10000
    for h in range(H):
        for w in range(W):
            tmp = 0
            for i in range(H):
                for j in range(W):
                    tmp += abs(A[h][w] - A[i][j])
            ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()