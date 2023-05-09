def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 200
    d = [0] * mod
    for i in range(n):
        d[a[i] % mod] += 1
    ans = 0
    for i in range(mod):
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()