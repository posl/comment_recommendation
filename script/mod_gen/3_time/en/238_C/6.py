def main():
    N = int(input())
    n = len(str(N))
    M = 998244353
    ans = 0
    for i in range(1,n):
        ans += 9*(10**(i-1))*i
        ans %= M
    ans += (N-(10**(n-1))+1)*n
    ans %= M
    print(ans)

if __name__ == '__main__':
    main()