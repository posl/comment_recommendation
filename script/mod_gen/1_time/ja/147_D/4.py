def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for k in range(60):
        cnt = 0
        for i in range(N):
            if (A[i] >> k) & 1:
                cnt += 1
        ans += (1 << k) * cnt * (N - cnt)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()