def solve(n, x, a, b):
    for i in range(n):
        if i % 2 == 0:
            x -= a[i]
        else:
            x -= b[i]
    return x >= 0
n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

if __name__ == '__main__':
    solve()