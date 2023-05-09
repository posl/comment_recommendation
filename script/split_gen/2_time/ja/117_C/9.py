def main():
    import sys
    from itertools import groupby
    N, M = map(int, sys.stdin.readline().split())
    X = sorted(map(int, sys.stdin.readline().split()))
    Xs = [list(g) for k, g in groupby(X)]
    print(sum(len(xs) - 1 for xs in Xs) + max(len(xs) - 1 for xs in Xs))
