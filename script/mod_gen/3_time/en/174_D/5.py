def solve():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        return 0
    if c[0] == 'R':
        return c[1:].count('W')
    else:
        return c.count('R')

if __name__ == '__main__':
    solve()