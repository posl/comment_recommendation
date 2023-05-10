def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    a = [i for i in range(n+1)]
    b = [i for i in range(n, -1, -1)]
    # print(a)
    # print(b)
    ans = 0
    for i in range(k, n+2):
        # print(i)
        # print(a[i])
        # print(b[i])
        ans += b[i] - a[i] + 1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()