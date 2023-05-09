def main():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    import itertools
    for x in itertools.permutations(S):
        X = '_'.join(x)
        if len(X) < 3 or len(X) > 16:
            continue
        if X not in T:
            print(X)
            return
    print(-1)
    return
