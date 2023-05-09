def solve():
    N, X = map(int, input().split())
    p = [1]
    for i in range(50):
        p.append(2*p[-1] + 1)
    def f(n, x):
        if n == 0:
            return 1
        if x == 1:
            return 0
        if x <= 1 + p[n-1]:
            return f(n-1, x-1)
        if x == 2 + p[n-1]:
            return 1 + f(n-1, x-2-p[n-1])
        if x <= 2 + 2*p[n-1]:
            return 1 + f(n-1, x-2-p[n-1])
        if x == 3 + 2*p[n-1]:
            return 2*p[n-1] + 1
    print(f(N, X))
