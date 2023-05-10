def solve():
    n,k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1<<n):
        t = set()
        for j in range(n):
            if i>>j&1:
                t |= set(s[j])
        if len(t) == k:
            ans = max(ans, len(t))
    print(ans)

if __name__ == '__main__':
    solve()