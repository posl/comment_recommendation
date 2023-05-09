def main():
    # Read the data
    N, M, K = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    # Solve the problem
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1
    for i in range(M):
        ans[A[i] - 1] -= 1
        ans[B[i] - 1] -= 1
    for i in range(K):
        if ans[C[i] - 1] > 0 and ans[D[i] - 1] > 0:
            ans[C[i] - 1] -= 1
            ans[D[i] - 1] -= 1
    for i in range(N):
        for j in range(M):
            if A[j] == i + 1 or B[j] == i + 1:
                ans[i] -= 1
    # Print the answer
    for i in range(N):
        print(ans[i], end = " ")
    print()
