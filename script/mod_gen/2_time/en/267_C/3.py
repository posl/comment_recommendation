def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N == M:
        ans = 0
        for i in range(N):
            ans += (i+1) * A[i]
        print(ans)
        return
    ans = -float("inf")
    for i in range(N-M+1):
        for j in range(i+M, N+1):
            tmp = 0
            for k in range(i, j):
                tmp += (k-i+1) * A[k]
            ans = max(ans, tmp)
    print(ans)
    return

if __name__ == '__main__':
    main()