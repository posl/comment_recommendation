def solve():
    # Implement solution here
    N, X = map(int, input().split())
    a = []
    b = []
    for _ in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    current = 0
    for i in range(N):
        current += a[i]
        if current > X:
            print('No')
            return
        if current == X:
            print('Yes')
            return
        current += b[i]
    if current == X:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()