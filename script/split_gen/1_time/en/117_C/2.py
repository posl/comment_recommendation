def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    d = []
    for i in range(m - 1):
        d.append(x[i + 1] - x[i])
    d.sort(reverse=True)
    ans = sum(d[n - 1:])
    print(ans)
