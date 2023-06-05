def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] > x:
            print('No')
            return
        x += b[i] - a[i]
    print('Yes')

if __name__ == '__main__':
    solve()