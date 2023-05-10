def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for i in range(Q)]
    S = sum(A)
    for i in range(Q):
        B,C = BC[i]
        S += (C-B)*A.count(B)
        print(S)
        A = [C if A[i]==B else A[i] for i in range(N)]
