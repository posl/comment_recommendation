def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    if n >= m:
        print('No')
        return
    if s == t[:n]:
        print('Yes')
    else:
        print('No')
solve()

if __name__ == '__main__':
    solve()