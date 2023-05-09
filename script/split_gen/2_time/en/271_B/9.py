def main():
    # get input
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        L, *a = map(int, input().split())
        A.append(a)
    S = []
    T = []
    for _ in range(Q):
        s, t = map(int, input().split())
        S.append(s)
        T.append(t)
    # solve
    ans = []
    for s, t in zip(S, T):
        ans.append(A[s - 1][t - 1])
    # output
    for a in ans:
        print(a)
