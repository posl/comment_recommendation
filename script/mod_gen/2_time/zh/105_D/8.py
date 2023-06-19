def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    d = {}
    for i in s:
        i %= m
        d[i] = d.get(i,0) + 1
    ans = 0
    for i in d.values():
        ans += i * (i - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()