def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] %= M
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = (sum_A[i] + A[i]) % M
    from collections import Counter
    c = Counter(sum_A)
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)
