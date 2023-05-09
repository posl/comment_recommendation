def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = A[0]
    for i in range(1, N):
        B[i] = B[i-1] + A[i]
    ans = 0
    for i in range(N-1):
        if B[i] < 0:
            ans += abs(B[i])
            B[i] = 0
    if B[N-1] < 0:
        ans += abs(B[N-1])
    print(ans)
