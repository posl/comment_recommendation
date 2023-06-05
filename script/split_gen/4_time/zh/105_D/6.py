def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    B = [x % M for x in S]
    from collections import Counter
    C = Counter(B)
    ans = 0
    for v in C.values():
        ans += v * (v - 1) // 2
    print(ans)
