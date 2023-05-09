def main():
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    S = []
    T = []
    for _ in range(Q):
        s, t = map(int, input().split())
        S.append(s)
        T.append(t)
    for i in range(Q):
        print(A[S[i]-1][T[i]-1])
main()
