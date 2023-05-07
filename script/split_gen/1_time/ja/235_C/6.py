def main():
    # input
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    Xs = [None] * Q
    Ks = [None] * Q
    for i in range(Q):
        Xs[i], Ks[i] = map(int, input().split())
    # compute
    As = [[As[i], i+1] for i in range(N)]
    As.sort()
    As.append([10**10, 0])
    # output
    for i in range(Q):
        l, r = 0, N
        while r-l > 1:
            m = (l+r)//2
            if As[m][0] <= Xs[i]:
                l = m
            else:
                r = m
        if As[l][0] == Xs[i]:
            print(As[l+Ks[i]-1][1])
        else:
            print(-1)
