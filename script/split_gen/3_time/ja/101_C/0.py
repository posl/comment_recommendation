def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    ans = 0
    for i in range(N):
        if B[i] > K:
            ans += 1
    print(ans)
