def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    ans = 0
    d = {}
    for i in range(N+1):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    for i in range(N+1):
        if A[i] + K in d:
            ans += d[A[i] + K]
    print(ans)
