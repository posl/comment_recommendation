def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        ans += (cnt * (n - cnt) * (1 << i))
    print(ans % (10 ** 9 + 7))

if __name__ == '__main__':
    main()