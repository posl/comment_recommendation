def solve(n, q, a, x):
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

if __name__ == '__main__':
    solve()