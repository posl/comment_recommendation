def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    B = [K - Q] * N
    for i in range(Q):
        B[A[i] - 1] += 1
    for i in range(N):
        print("Yes" if B[i] > 0 else "No")
