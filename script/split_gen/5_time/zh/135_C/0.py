def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0] * (N + 1)
    for i in range(N):
        C[i] = A[i] - B[i]
        C[i + 1] = A[i + 1]
    ans = 0
    for i in range(N + 1):
        if C[i] > 0:
            ans += B[i]
        else:
            ans += A[i]
    print(ans)
