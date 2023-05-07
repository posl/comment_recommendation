def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(k,n+2):
        ans += i*n - i*(i-1) + 1
        ans = ans % (10**9+7)
    print(ans)

if __name__ == '__main__':
    main()