def solve(n, s, a, b):
    for i in range(1 << n):
        t = 0
        for j in range(n):
            if (i >> j) & 1:
                t += a[j]
            else:
                t += b[j]
        if t == s:
            return "Yes" + "
" + "".join(["T" if (i >> j) & 1 else "H" for j in range(n)])
    return "No"
n, s = map(int, input().split())
a, b = [], []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
print(solve(n, s, a, b))

if __name__ == '__main__':
    solve()