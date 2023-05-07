def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0] * N
    ans[0] = -1
    for i in range(M):
        if A[i] == 1:
            ans[B[i] - 1] = 1
        if B[i] == 1:
            ans[A[i] - 1] = 1
    if 0 in ans:
        print('No')
    else:
        print('Yes')
        for i in range(N - 1):
            print(ans[i])
