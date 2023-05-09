def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for a in A:
            if a & 1:
                cnt += 1
            a >>= 1
        ans += cnt * (N - cnt) * (2 ** i)
        ans %= mod
    print(ans)
main()

if __name__ == '__main__':
    main()