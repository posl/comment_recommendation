def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a[:m])
    t = sum([i*a[i] for i in range(m)])
    ans = t
    for i in range(m,n):
        t += (m-1)*a[i] - 2*s + a[i-m]
        ans = max(ans, t)
        s += a[i] - a[i-m]
    print(ans)
main()
