def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        min = i*(i-1)//2
        max = i*(2*n-i+1)//2
        ans += max - min + 1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()