def solve():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    if N == 1:
        print(-1)
        return
    if N == 2:
        print(2)
        print('1 1')
        print('LR')
        print('RL')
        return
    if N == 3:
        print(2)
        print('1 2')
        print('RL')
        print('UU')
        print('DR')
        return
    print(5)
    print('3 1 4 1 5')
    print('LRDUL')
    print('RDULR')
    print('DULRD')
    return
