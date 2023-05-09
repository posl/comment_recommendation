def main():
    N = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += N//(10**i)*(10**(i-1))
        ans %= mod
        if N%(10**i) >= 10**(i-1):
            ans += 10**(i-1)
            ans %= mod
        else:
            ans += N%(10**i) + 1
            ans %= mod
    print(ans)
main()

if __name__ == '__main__':
    main()