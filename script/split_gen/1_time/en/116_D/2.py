def solve():
    N, K = map(int, input().split())
    T = [0] * N
    D = [0] * N
    for i in range(N):
        t, d = map(int, input().split())
        T[i] = t - 1
        D[i] = d
    D.sort(reverse=True)
    T.sort()
    T.append(N)
    cnt = [0] * N
    for i in range(N):
        cnt[T[i]] += 1
    cnt.sort(reverse=True)
    K = min(K, N - cnt.count(0))
    ans = 0
    tmp = 0
    for i in range(N):
        tmp += D[i]
        if cnt[T[i]] > 0:
            cnt[T[i]] -= 1
            K -= 1
        if K == 0:
            ans = max(ans, tmp + K * K)
        else:
            ans = max(ans, tmp + K * K)
    print(ans)
