def main():
    N, Q = map(int, input().split())
    L = [0] * N
    A = [0] * N
    for i in range(N):
        L[i] = list(map(int, input().split()))
        A[i] = L[i].pop(0)
    S = [0] * Q
    T = [0] * Q
    for i in range(Q):
        s, t = map(int, input().split())
        S[i] = s
        T[i] = t
    for i in range(Q):
        print(L[S[i]-1][T[i]-1])
main()
