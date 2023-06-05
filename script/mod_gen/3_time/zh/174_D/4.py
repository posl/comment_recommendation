def solve():
    N = int(input())
    c = input()
    c = list(c)
    r = c.count('R')
    w = c.count('W')
    ans = 0
    for i in range(r):
        if c[i] == 'W':
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()