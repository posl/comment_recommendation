def solve(n, m, a, b):
    work = []
    for i in range(n):
        work.append([a[i], b[i]])
    work.sort()
    ans = 0
    for i in range(n):
        if m > work[i][0]:
            m += work[i][1]
            ans += work[i][1]
        else:
            break
    print(ans)
n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
solve(n, m, a, b)

if __name__ == '__main__':
    solve()