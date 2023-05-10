def solve():
    n = int(input())
    s = [input() for i in range(n)]
    ans = 0
    for i in range(10):
        t = 0
        for j in range(n):
            t = max(t, s[j].index(str(i)))
        ans = max(ans, t)
    print(ans)
solve()

if __name__ == '__main__':
    solve()