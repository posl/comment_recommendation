def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    b = []
    prev = -1
    for i in range(n + 1):
        if a[i] != prev:
            b.append([a[i], 1])
            prev = a[i]
        else:
            b[-1][1] += 1
    c = [0] * len(b)
    for i in range(len(b) - 1):
        c[i + 1] = c[i] + b[i][1]
    ans = 0
    for i in range(len(b)):
        if b[i][0] - c[i] > 0:
            ans += b[i][0] - c[i]
    print(ans)

if __name__ == '__main__':
    solve()