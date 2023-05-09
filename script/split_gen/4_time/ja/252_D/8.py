def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    cnt = [0] * (2 * 10 ** 5 + 1)
    for i in range(1, N + 1):
        cnt[A[i]] += 1
    for i in range(1, 2 * 10 ** 5 + 1):
        cnt[i] += cnt[i - 1]
    ans = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if 2 * A[j] - A[i] > 2 * 10 ** 5:
                break
            ans += cnt[2 * A[j] - A[i]] - cnt[A[j]]
    print(ans)
