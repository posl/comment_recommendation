def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(N):
        A[i + 1] = (A[i] + A[i + 1]) % M
    from collections import Counter
    C = Counter(A)
    ans = 0
    for c in C.values():
        ans += c * (c - 1) // 2
    print(ans)
solve()

if __name__ == '__main__':
    solve()