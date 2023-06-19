def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    from collections import Counter
    cnt = Counter()
    for a in A:
        cnt[a % M] += 1
    ans = 0
    for c in cnt.values():
        ans += c * (c-1) // 2
    print(ans)
