def solve():
    # Implement solution here
    N = int(input())
    XY = []
    for i in range(N):
        XY.append(tuple(map(int, input().split())))
    S = input()
    for i in range(N-1):
        for j in range(i+1, N):
            if XY[i][0] < XY[j][0]:
                if S[i] == 'R' and S[j] == 'L':
                    if XY[i][1] <= XY[j][1] and XY[j][1] <= XY[i][1] + 1:
                        print('Yes')
                        return
            elif XY[i][0] > XY[j][0]:
                if S[i] == 'L' and S[j] == 'R':
                    if XY[j][1] <= XY[i][1] and XY[i][1] <= XY[j][1] + 1:
                        print('Yes')
                        return
    print('No')
    return
