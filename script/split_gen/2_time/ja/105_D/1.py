def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    ans = 0
    cnt = [0] * M
    for i in range(N + 1):
        ans += cnt[sum_A[i] % M]
        cnt[sum_A[i] % M] += 1
    print(ans)
