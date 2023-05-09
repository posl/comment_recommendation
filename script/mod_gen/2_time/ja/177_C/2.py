def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    s = sum(a)
    ans = 0
    for i in a:
        s -= i
        ans += i*s
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()