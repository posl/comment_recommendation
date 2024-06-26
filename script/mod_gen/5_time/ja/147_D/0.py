def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        one = 0
        zero = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                one += 1
            else:
                zero += 1
        ans += (one * zero * pow(2, i, 10**9+7))
        ans %= 10**9+7
    print(ans)

if __name__ == '__main__':
    main()