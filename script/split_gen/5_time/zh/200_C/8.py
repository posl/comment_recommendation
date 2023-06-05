def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 200
    for i in range(n):
        cnt[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)
