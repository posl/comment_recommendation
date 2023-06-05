def main():
    X = input()
    M = int(input())
    d = int(max(X))
    #print(X, M, d)
    def f(n, s):
        if s == 0:
            return 0
        else:
            return n * f(n, s - 1) + 1
    def g(n, s):
        if s == 0:
            return 0
        else:
            return n * g(n, s - 1) + n ** (s - 1)
    def h(n, s, m):
        if s == 0:
            return 0
        else:
            return n * h(n, s - 1, m) + min(n - 1, m // n ** (s - 1))
    def solve(n):
        if n == 0:
            return 1
        else:
            return h(n, len(X), M) - h(n, len(X) - 1, M)
    ans = 0
    for n in range(d + 1, 100):
        ans += solve(n)
    print(ans)
