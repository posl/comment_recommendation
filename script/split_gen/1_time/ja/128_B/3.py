def solve():
    N = int(input())
    S = [0]*N
    P = [0]*N
    for i in range(N):
        S[i], P[i] = input().split()
        P[i] = int(P[i])
    for i in range(N):
        print(P.index(max(P))+1)
        P[P.index(max(P))] = -1
