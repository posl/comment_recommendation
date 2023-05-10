def main():
    N = int(input())
    mod = 998244353
    ans = 0
    tmp = 10
    while tmp <= N:
        ans += (N//tmp)*(tmp//10)
        ans += max(0, (N%tmp) - (tmp//10) + 1)
        ans %= mod
        tmp *= 10
    print(ans)

if __name__ == '__main__':
    main()