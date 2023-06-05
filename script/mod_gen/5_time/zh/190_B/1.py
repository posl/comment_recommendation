def solve():
    N, S, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    for x, y in XY:
        if x < S and y > D:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    solve()