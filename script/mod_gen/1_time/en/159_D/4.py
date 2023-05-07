def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0 for i in range(N + 1)]
    for a in A:
        cnt[a] += 1
    ans = [0 for i in range(N)]
    for i in range(N):
        ans[i] = N - 1 - cnt[A[i]]
    for i in range(N):
        if cnt[A[i]] > 1:
            ans[i] += cnt[A[i]] * (cnt[A[i]] - 1) // 2
    print(*ans, sep='
')

if __name__ == '__main__':
    main()