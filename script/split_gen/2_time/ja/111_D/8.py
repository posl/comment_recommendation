def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(1)
        print(1)
        print(1)
        return
    if N == 2:
        if XY[0] == XY[1]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        else:
            print(-1)
            return
    # N >= 3
    m = 40
    d = [1] + [2 ** i for i in range(1, m)]
    w = [''] * N
    for i in range(N):
        for j in range(m):
            if XY[i][0] & (1 << j):
                w[i] += 'R'
            else:
                w[i] += 'L'
            if XY[i][1] & (1 << j):
                w[i] += 'U'
            else:
                w[i] += 'D'
    print(m)
    print(*d)
    for wi in w:
        print(wi)
