def main():
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        res += cnt * (n - cnt) * pow(2, i, 10**9+7)
        res %= 10**9+7
    print(res)

if __name__ == '__main__':
    main()