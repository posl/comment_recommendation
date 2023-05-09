def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    ans = 0
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N+1):
        d[A[i]] += 1
        if A[i] - K in d:
            ans += d[A[i] - K]
    print(ans)
