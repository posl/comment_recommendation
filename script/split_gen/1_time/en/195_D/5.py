def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        A = X[:L-1] + X[R:]
        A.sort()
        ans = 0
        for j in range(N):
            for k in range(len(A)):
                if W[j] <= A[k]:
                    ans += V[j]
                    A[k] = -1
                    break
        print(ans)
