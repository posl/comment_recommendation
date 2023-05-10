def main():
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        exit()
    ans = 0
    d = []
    for i in range(m-1):
        d.append(x[i+1]-x[i])
    d.sort(reverse=True)
    for i in range(n-1):
        ans += d[i]
    print(ans)
