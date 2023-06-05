def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0 for i in range(n)]
    for i in range(n):
        cnt[a[i]-1] += 1
    for i in range(n):
        ans += cnt[i] * (cnt[i]-1) // 2
    print(ans)
