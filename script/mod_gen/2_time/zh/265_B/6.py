def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    now = 0
    for x, y in XY:
        if now + A[x - 1] >= T:
            print('No')
            return
        now += A[x - 1] + y
    if now + A[-1] >= T:
        print('No')
        return
    print('Yes')

if __name__ == '__main__':
    solve()