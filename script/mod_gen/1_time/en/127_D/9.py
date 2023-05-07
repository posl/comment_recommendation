def solve(n, m, a, b, c):
    a.sort()
    for i in range(m):
        for j in range(b[i]):
            if a[j] < c[i]:
                a[j] = c[i]
            else:
                break
        a.sort()
    return sum(a)
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = []
c = []
for i in range(m):
    bi, ci = map(int, input().split())
    b.append(bi)
    c.append(ci)
print(solve(n, m, a, b, c))

if __name__ == '__main__':
    solve()