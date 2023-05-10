def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if n % 2 == 0:
        m1 = (a[n//2-1] + a[n//2]) / 2
        m2 = (b[n//2-1] + b[n//2]) / 2
        print(int((m2-m1)*2+1))
    else:
        m = (b[n//2] - a[n//2])
        print(m+1)
    return 0

if __name__ == '__main__':
    solve()