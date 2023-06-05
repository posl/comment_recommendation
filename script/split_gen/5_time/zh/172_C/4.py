def solve():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(N):
        if cnt + A[i] > K:
            break
        cnt += A[i]
        ans += 1
    for i in range(M):
        while cnt + B[i] <= K and ans < N + M:
            cnt += B[i]
            ans += 1
        if cnt + B[i] > K:
            cnt -= A[ans - 1]
            ans -= 1
            break
    print(ans)
solve()
