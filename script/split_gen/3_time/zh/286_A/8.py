def get_input():
    N, P, Q, R, S = input().split()
    N = int(N)
    P = int(P)
    Q = int(Q)
    R = int(R)
    S = int(S)
    A = input().split()
    A = [int(x) for x in A]
    return N, P, Q, R, S, A
