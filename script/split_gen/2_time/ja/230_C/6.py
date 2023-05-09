def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    def f(x, y):
        return x * (x + 1) // 2 * (N - y + 1) + (N - x + 1) * (N - x) // 2 * y
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            print('#' if f(i, j) - f(i, B) - f(A, j) + f(A, B) > 0 else '.', end='')
        print()
