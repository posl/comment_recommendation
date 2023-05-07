def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    ans = 0
    cnt = {}
    for i in range(N + 1):
        if A[i] - K in cnt:
            ans += cnt[A[i] - K]
        if A[i] in cnt:
            cnt[A[i]] += 1
        else:
            cnt[A[i]] = 1
    print(ans)
