def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(n+1)
    if m == 0:
        print(1)
        return
    if m == n:
        print(0)
        return
    d = []
    for i in range(m):
        d.append(a[i+1] - a[i] - 1)
    d.sort()
    k = d[0]
    for i in range(m-1):
        d[i+1] -= k
        if d[i+1] < 0:
            d[i+1] = 0
    print(sum(d) // k + 1)
