def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0 for _ in range(M)]
    ans[0] = N * (N - 1) // 2
    cnt = [1 for _ in range(N + 1)]
    for i in range(1, M):
        a, b = AB[i - 1]
        ans[i] = ans[i - 1]
        if cnt[a] > cnt[b]:
            a, b = b, a
        if cnt[a] > 0:
            ans[i] -= cnt[a] * (cnt[a] - 1) // 2
        if cnt[b] > 0:
            ans[i] -= cnt[b] * (cnt[b] - 1) // 2
        cnt[a] += cnt[b]
        cnt[b] = 0
        if cnt[a] > 0:
            ans[i] += cnt[a] * (cnt[a] - 1) // 2
    ans.reverse()
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()