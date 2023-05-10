def main():
    # input
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    # compute
    XY.sort()
    XY = list(map(list, zip(*XY)))
    Xs = XY[0]
    Ys = XY[1]
    if (Xs[0] < Xs[-1] and S.count('L') == 0) or (Xs[0] > Xs[-1] and S.count('R') == 0):
        print('No')
    elif (Ys[0] < Ys[-1] and S.count('D') == 0) or (Ys[0] > Ys[-1] and S.count('U') == 0):
        print('No')
    else:
        print('Yes')
