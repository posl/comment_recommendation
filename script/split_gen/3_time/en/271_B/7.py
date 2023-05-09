def main():
    import sys
    from itertools import accumulate
    N, Q = map(int, sys.stdin.readline().split())
    L = []
    A = []
    for i in range(N):
        l = list(map(int, sys.stdin.readline().split()))
        L.append(l[0])
        A.append(l[1:])
    S = []
    T = []
    for i in range(Q):
        s, t = map(int, sys.stdin.readline().split())
        S.append(s)
        T.append(t)
    C = [0] + list(accumulate(L))
    for i in range(Q):
        print(A[S[i]-1][T[i]-1])
    return
main()
