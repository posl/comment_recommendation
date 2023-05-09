def main():
    A, B = map(int, input().split())
    def f(g):
        return A / (g ** 0.5)
    def g(t):
        return B * t + f(t)
    def h(t):
        return B * t + f(t + 1)
    def ternary_search(l, r, f):
        while r - l > 10 ** -6:
            c1 = (2 * l + r) / 3
            c2 = (l + 2 * r) / 3
            if f(c1) < f(c2):
                r = c2
            else:
                l = c1
        return f(l)
    print(ternary_search(0, 10 ** 9, g))
