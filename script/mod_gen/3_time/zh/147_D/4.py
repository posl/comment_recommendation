def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        ans += (1 << i) * cnt * (n - cnt)
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()