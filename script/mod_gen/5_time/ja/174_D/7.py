def solve():
    n = int(input())
    s = input()
    r = s.count('R')
    w = s.count('W')
    ans = min(r, w)
    r = s[:r].count('W')
    w = s[:w].count('R')
    ans = min(ans, max(r, w))
    print(ans)

if __name__ == '__main__':
    solve()