def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    d = {}
    d[0] = 1
    for i in range(n):
        s += a[i]
        if s - k in d:
            ans += d[s - k]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(ans)
main()
