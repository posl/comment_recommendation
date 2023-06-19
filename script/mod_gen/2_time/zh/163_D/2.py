def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    if k>n:
        print(0)
        return
    if k==n:
        print(1)
        return
    if k==n-1:
        print(n)
        return
    ans = 0
    for i in range(k,n+1):
        ans += i*(n-i+1)+1
    print(ans%mod)

if __name__ == '__main__':
    main()