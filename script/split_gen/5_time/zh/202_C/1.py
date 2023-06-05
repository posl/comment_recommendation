def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    d = [0] * n
    e = [0] * n
    f = [0] * n
    for i in range(n):
        d[a[i] - 1] += 1
        e[b[c[i] - 1] - 1] += 1
        f[c[i] - 1] += 1
    ans = 0
    for i in range(n):
        ans += d[i] * e[i]
    print(ans)
