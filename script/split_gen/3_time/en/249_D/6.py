def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    Amax = max(A)
    cnt = [0] * (Amax + 1)
    for i in range(N):
        cnt[A[i]] += 1
    ans = 0
    for i in range(1, Amax + 1):
        if cnt[i] >= 2:
            ans += cnt[i] * (cnt[i] - 1) // 2
        for j in range(2 * i, Amax + 1, i):
            ans += cnt[i] * cnt[j]
    print(ans)
