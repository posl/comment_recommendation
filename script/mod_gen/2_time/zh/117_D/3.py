def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        if cnt <= n//2:
            if ans + (1 << i) <= k:
                ans += 1 << i
    s = 0
    for i in range(n):
        s += ans ^ a[i]
    print(s)

if __name__ == '__main__':
    solve()