def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    def f(x):
        if x <= 0:
            return 0
        y = min(N, x)
        return y * (y + 1) // 2
    def g(x):
        if x <= 0:
            return 0
        y = min(N, x)
        return y * (y + 1) * (2 * y + 1) // 6
    def h(x):
        if x <= 0:
            return 0
        y = min(N, x)
        return y * (y + 1) // 2 * (2 * y + 1) // 3
    def calc(x, y):
        return f(x) * f(y) + g(x) * f(y) + f(x) * g(y) + h(x) * f(y) + f(x) * h(y)
    def solve(x, y):
        return calc(x, y) - calc(x - A, y - B) - calc(x - A, y - B + N) - calc(x - A + N, y - B) - calc(x - A + N, y - B + N)
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            print('#' if solve(i, j) % 2 else '.', end='')
        print()
