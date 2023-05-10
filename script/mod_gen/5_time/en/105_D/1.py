def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = (S[i] + A[i]) % M
    from collections import Counter
    C = Counter(S)
    ans = 0
    for k, v in C.items():
        ans += v * (v - 1) // 2
    print(ans)
solve()

if __name__ == '__main__':
    solve()