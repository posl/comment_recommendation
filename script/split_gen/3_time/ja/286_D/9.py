def main():
    # input
    N, X = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(N)]
    # compute
    for i in range(N):
        if ABs[i][0]*ABs[i][1] >= X:
            ABs[i][1] = X//ABs[i][0]
            X -= ABs[i][0]*ABs[i][1]
        else:
            X -= ABs[i][0]*ABs[i][1]
    # output
    if X == 0:
        print('Yes')
    else:
        print('No')
