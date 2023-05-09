def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if K <= N:
        for i in range(N):
            print(K)
        return
    K -= N
    cnt = [0] * N
    for i in range(1, N):
        cnt[i] = cnt[i-1] + (a[i] - a[i-1]) * i
    cnt.append(K + 1)
    start = 0
    end = N
    while end - start > 1:
        mid = (start + end) // 2
        if cnt[mid] <= K:
            start = mid
        else:
            end = mid
    ans = [0] * N
    for i in range(N):
        ans[i] = (K - cnt[start]) // (start + 1) + a[i]
    for i in range(K - cnt[start] - (K - cnt[start]) // (start + 1) * (start + 1)):
        ans[i] += 1
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()