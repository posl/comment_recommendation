def main():
    A, B, Q = [int(i) for i in input().split()]
    s = [int(input()) for i in range(A)]
    t = [int(input()) for i in range(B)]
    x = [int(input()) for i in range(Q)]
    s = [-float('inf')] + s + [float('inf')]
    t = [-float('inf')] + t + [float('inf')]
    import bisect
    for xi in x:
        si = bisect.bisect_left(s, xi)
        ti = bisect.bisect_left(t, xi)
        print(min(max(s[si], t[ti]) - xi, xi - min(s[si - 1], t[ti - 1]), 2 * (xi - s[si - 1]) + t[ti] - xi, 2 * (t[ti - 1] - xi) + xi - s[si]))
