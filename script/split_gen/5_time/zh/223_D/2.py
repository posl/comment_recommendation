def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [0] * N
    for i in range(M):
        ans[B[i] - 1] = A[i]
    if ans[0] == 0:
        ans[0] = 1
    for i in range(1, N):
        if ans[i] == 0:
            ans[i] = ans[i - 1] + 1
    if len(set(ans)) != N:
        print(-1)
    else:
        print(*ans)
