def solve():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    s = [list(i) for i in zip(*s)]
    t = [list(i) for i in zip(*t)]
    s.sort()
    t.sort()
    print('Yes' if s == t else 'No')

if __name__ == '__main__':
    solve()