def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    ans = 0
    for i in range(1, N):
        ans = max(ans, B[0] - A[-1], B[-1] - A[0])
    print(ans)
