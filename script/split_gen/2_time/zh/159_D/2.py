def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] += 1
    ans = 0
    for i in range(N):
        ans += B[i] * (B[i] - 1) // 2
    for i in range(N):
        print(ans - (B[A[i] - 1] - 1))
