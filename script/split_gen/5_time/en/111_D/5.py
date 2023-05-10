def solve():
    n = int(input())
    xys = [list(map(int, input().split())) for _ in range(n)]
    if n == 1:
        print(-1)
        return
    if n == 2:
        if xys[0] == xys[1]:
            print(-1)
            return
        print(2)
        print(1, 1)
        print('LR')
        print('RL')
        return
    print(5)
    print(3, 1, 4, 1, 5)
    print('LRDUL')
    print('RDULR')
    print('DULRD')
    return
solve()
