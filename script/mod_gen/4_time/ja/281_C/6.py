def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    now = 0
    for i in range(n):
        if t < a[i]:
            ans = i + 1
            now = t
            break
        else:
            t -= a[i]
    else:
        ans = (t // sum(a)) * n + 1
        now = t % sum(a)
    print(ans, now)

if __name__ == '__main__':
    solve()