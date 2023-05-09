def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # A[i]からA[j]までの和をsum[i][j]とする
    sum = [[0 for i in range(N)] for j in range(N)]
    ans = 0
    for i in range(N):
        sum[i][i] = A[i]
        if sum[i][i] == K:
            ans += 1
        for j in range(i+1, N):
            sum[i][j] = sum[i][j-1] + A[j]
            if sum[i][j] == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()