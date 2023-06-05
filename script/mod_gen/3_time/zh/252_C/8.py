def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 10**10
    for i in range(n):
        t = 0
        for j in range(n):
            t += min((i-j)%n, (j-i)%n)
        ans = min(ans, t)
    print(ans)

if __name__ == '__main__':
    solve()