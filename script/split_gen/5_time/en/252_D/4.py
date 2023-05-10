def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (N + 1)
    for a in A:
        cnt[a] += 1
    ans = 0
    for i in range(1, N + 1):
        ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    for i in range(1, N + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2 * (N - cnt[i])
    print(ans)
main()
