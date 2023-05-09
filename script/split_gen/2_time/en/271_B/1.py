def main():
    N, Q = list(map(int, input().split()))
    L = []
    A = []
    for i in range(N):
        l = list(map(int, input().split()))
        L.append(l[0])
        A.append(l[1:])
    S = []
    T = []
    for i in range(Q):
        s, t = list(map(int, input().split()))
        S.append(s)
        T.append(t)
    for i in range(Q):
        print(A[S[i]-1][T[i]-1])
