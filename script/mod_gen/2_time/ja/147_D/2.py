def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt0 = 0
        cnt1 = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt1 += 1
            else:
                cnt0 += 1
        ans += cnt0 * cnt1 * (2 ** i)
        ans %= 10 ** 9 + 7
    print(ans)

if __name__ == '__main__':
    main()