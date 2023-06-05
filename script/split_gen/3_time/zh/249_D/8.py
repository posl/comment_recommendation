def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0] * (max(a) + 1)
    for i in range(n):
        cnt[a[i]] += 1
    for i in range(n):
        for j in range(1, int(a[i] ** 0.5) + 1):
            if a[i] % j == 0:
                if j * j == a[i]:
                    ans += cnt[j] * (cnt[j] - 1)
                else:
                    ans += cnt[j] * cnt[a[i] // j]
    print(ans // 2)
main()
