def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    d = []
    for i in range(n):
        d.append(a[i] - b[i])
    c.sort()
    d.sort()
    print(min(c[n - 1], sum(d[n - 1:n + 1])))
main()
