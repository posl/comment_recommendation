def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    # 1,2,...,N の順列を作成
    # 1,2,...,N の順列を作成
    def perm(N):
        if N == 1:
            return [[1]]
        else:
            return [[N] + p for p in perm(N-1)] + [p + [N] for p in perm(N-1)]
    # 1,2,...,N の順列を作成
    # 1,2,...,N の順列を作成
    def perm(N):
        if N == 1:
            return [[1]]
        else:
            return [[N] + p for p in perm(N-1)] + [p + [N] for p in perm(N-1)]
    Pp = perm(N)
    #print(Pp)
    #print(P)
    #print(Q)
    #print(Pp.index(P))
    #print(Pp.index(Q))
    print(abs(Pp.index(P) - Pp.index(Q)))
