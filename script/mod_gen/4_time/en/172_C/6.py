def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_cumsum = [0] * (N + 1)
    B_cumsum = [0] * (M + 1)
    for i in range(N):
        A_cumsum[i + 1] = A_cumsum[i] + A[i]
    for i in range(M):
        B_cumsum[i + 1] = B_cumsum[i] + B[i]
    ans = 0
    for i in range(N + 1):
        if A_cumsum[i] > K:
            break
        ok = -1
        ng = M + 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if A_cumsum[i] + B_cumsum[mid] <= K:
                ok = mid
            else:
                ng = mid
        ans = max(ans, i + ok)
    print(ans)

if __name__ == '__main__':
    main()