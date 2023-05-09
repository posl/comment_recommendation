def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    cnt = [0] * (N + 1)
    for i in range(1, N + 1):
        cnt[A[i]] += 1
    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        ans[i] = (cnt[A[i]] - 1) * (N - cnt[A[i]]) + cnt[A[i]] * (cnt[A[i]] - 1) // 2
    for i in range(1, N + 1):
        print(ans[i])
