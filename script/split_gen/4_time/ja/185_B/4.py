def solve():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[0])
    battery = N
    for i in range(M):
        battery -= AB[i][0]
        if battery <= 0:
            print('No')
            return
        battery = min(battery + AB[i][1] - AB[i][0], N)
    battery -= T - AB[-1][1]
    if battery <= 0:
        print('No')
    else:
        print('Yes')
