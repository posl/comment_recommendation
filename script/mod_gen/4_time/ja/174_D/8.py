def solve():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    ans = min(r, w)
    r = c[:r].count('W')
    w = c[w:].count('R')
    ans += min(r, w)
    print(ans)

if __name__ == '__main__':
    solve()