def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    C = [0] * M
    for i in range(M):
        B[i], C[i] = map(int, input().split())
    A.sort()
    B, C = zip(*sorted(zip(B, C), key=lambda x: x[1], reverse=True))
    ans = 0
    for i in range(N):
        if i < M and C[i] > A[i]:
            ans += C[i]
        else:
            ans += A[i]
    print(ans)
