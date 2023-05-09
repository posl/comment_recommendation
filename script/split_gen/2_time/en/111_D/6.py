def solve():
    N = int(input())
    p = [tuple(map(int, input().split())) for _ in range(N)]
    if N <= 2:
        print(2)
        print(1, 1)
        for i in range(N):
            print('RU')
        return
    if p[0] != p[1]:
        d = abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])
        print(2)
        print(d, d)
        for i in range(N):
            print('RU')
        return
    for i in range(2, N):
        if p[0] != p[i]:
            d1 = abs(p[0][0] - p[i][0]) + abs(p[0][1] - p[i][1])
            d2 = abs(p[1][0] - p[i][0]) + abs(p[1][1] - p[i][1])
            if d1 % 2 != d2 % 2:
                print(2)
                print(d1, d2)
                for i in range(N):
                    print('RU')
                return
            print(3)
            print(d1, d1, d2)
            for i in range(N):
                print('RUR')
            return
    print(-1)
