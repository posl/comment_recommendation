def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        zero = 0
        one = 0
        for j in range(n):
            if a[j] & (1 << i):
                one += 1
            else:
                zero += 1
        ans += (zero * one) * (1 << i)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()