def main():
    # input
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    Xs = [None]*Q
    Ks = [None]*Q
    for i in range(Q):
        Xs[i], Ks[i] = map(int, input().split())
    # compute
    Ds = {}
    for i, A in enumerate(As, 1):
        if A in Ds:
            Ds[A].append(i)
        else:
            Ds[A] = [i]
    ans = []
    for i in range(Q):
        X = Xs[i]
        K = Ks[i]
        if X in Ds and K <= len(Ds[X]):
            ans.append(Ds[X][K-1])
        else:
            ans.append(-1)
    # output
    for i in range(Q):
        print(ans[i])
