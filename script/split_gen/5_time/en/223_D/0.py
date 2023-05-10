def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [0] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(M):
        if ans[A[i] - 1] > ans[B[i] - 1]:
            ans[A[i] - 1], ans[B[i] - 1] = ans[B[i] - 1], ans[A[i] - 1]
    for i in range(N - 1):
        if ans[i] > ans[i + 1]:
            print(-1)
            exit()
    print(" ".join(map(str, ans)))
