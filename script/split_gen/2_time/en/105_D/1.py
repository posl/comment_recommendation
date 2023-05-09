def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = (B[i] + A[i]) % M
    d = {}
    for i in range(N + 1):
        d.setdefault(B[i], 0)
        d[B[i]] += 1
    ans = 0
    for k, v in d.items():
        ans += v * (v - 1) // 2
    print(ans)
