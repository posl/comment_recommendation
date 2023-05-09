def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 累積和
    C = [0] * (N + 1)
    for i in range(N):
        C[i + 1] = (C[i] + A[i]) % (10 ** 9 + 7)
    ans = 0
    for i in range(N):
        ans += A[i] * (C[N] - C[i + 1])
        ans %= (10 ** 9 + 7)
    print(ans)
