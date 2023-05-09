def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(60):
        zero = 0
        one = 0
        for a in A:
            if (a >> i) & 1:
                one += 1
            else:
                zero += 1
        ans += (zero * one) * (2**i)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()