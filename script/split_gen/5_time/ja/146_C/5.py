def main():
    A, B, X = map(int, input().split())
    def f(N):
        return A * N + B * len(str(N))
    l = 0
    r = 10 ** 9 + 1
    while r - l > 1:
        m = (l + r) // 2
        if f(m) <= X:
            l = m
        else:
            r = m
    print(l)
