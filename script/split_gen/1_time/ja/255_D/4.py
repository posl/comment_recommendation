def main():
    import sys
    from itertools import accumulate
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    a = [0] + A
    acc = list(accumulate(a))
    for x in X:
        if x >= acc[-1]:
            print(N * x - acc[-1])
            continue
        l, r = 0, N
        while r - l > 1:
            m = (l + r) // 2
            if acc[m] <= x:
                l = m
            else:
                r = m
        print((N - l) * x - (acc[-1] - acc[l]))
