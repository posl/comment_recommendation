def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    L = [a[0] for a in A]
    A = [a[1:] for a in A]
    #print(N, X)
    #print(L)
    #print(A)
    from collections import defaultdict
    d = defaultdict(int)
    d[1] = 1
    for i in range(N):
        d2 = defaultdict(int)
        for k, v in d.items():
            for j in range(L[i]):
                d2[k*A[i][j]] += v
        d = d2
    print(d[X])
