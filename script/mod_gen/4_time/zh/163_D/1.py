def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += i*(2*n-i+1)//2 - i*(i-1)//2 + 1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()