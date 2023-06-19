def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    S = S.replace('L', '1').replace('R', '0')
    S = S[::-1]
    S = int(S, 2)
    XY.sort(key=lambda x: x[0])
    for i in range(N):
        XY[i][0] -= i
    XY.sort(key=lambda x: x[1])
    for i in range(N):
        XY[i][1] -= i
    XY.sort(key=lambda x: x[0] + x[1])
    for i in range(N):
        XY[i][0] += i
    XY.sort(key=lambda x: x[0])
    for i in range(N):
        XY[i][1] += i
    XY.sort(key=lambda x: x[0] + x[1])
    for i in range(N):
        if XY[i][0] + XY[i][1] == XY[0][0] + XY[0][1]:
            if S >> i & 1:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    solve()