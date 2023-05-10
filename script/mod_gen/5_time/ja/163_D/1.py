def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        #print(i)
        ans += i*(n+1-i+1)+1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()