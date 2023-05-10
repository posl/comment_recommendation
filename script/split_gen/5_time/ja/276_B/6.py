def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(M):
        ans[A[i]][0] += 1
        ans[B[i]][0] += 1
        ans[A[i]][ans[A[i]][0]] = B[i]
        ans[B[i]][ans[B[i]][0]] = A[i]
    for i in range(1, N + 1):
        print(ans[i][0], end = "")
        for j in range(1, ans[i][0] + 1):
            print(" " + str(ans[i][j]), end = "")
        print("")
