def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(60):
        cnt0 = 0
        cnt1 = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt1 += 1
            else:
                cnt0 += 1
        ans += (cnt0 * cnt1) * (2 ** i)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()