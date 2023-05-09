def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(60):
        a = 0
        b = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                a += 1
            else:
                b += 1
        ans += a * b * pow(2, i, MOD)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()