def solve():
    N = int(input())
    XY = []
    for _ in range(N):
        XY.append(list(map(int, input().split())))
    S = input()
    for i in range(N):
        XY[i].append(S[i])
    XY.sort(key=lambda x: x[0])
    for i in range(1, N):
        if XY[i][2] == 'L' and XY[i - 1][2] == 'R':
            if XY[i][1] >= XY[i - 1][1]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    solve()