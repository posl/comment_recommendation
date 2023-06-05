def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 1<<60
    for i in range(n):
        for j in range(10):
            t = 0
            for k in range(n):
                d = (i+k)%n
                t += min(abs(j-int(s[d][k])), 10-abs(j-int(s[d][k])))
            ans = min(ans, t)
    print(ans)

if __name__ == '__main__':
    solve()