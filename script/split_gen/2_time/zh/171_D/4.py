def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    print(N, A, Q, BC)
    for i in range(Q):
        B = BC[i][0]
        C = BC[i][1]
        for j in range(N):
            if A[j] == B:
                A[j] = C
        print(sum(A))
