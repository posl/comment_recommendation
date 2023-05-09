def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    L = LR[0][0]
    R = LR[0][1]
    for i in range(1, N):
        if LR[i][0] <= R:
            R = max(R, LR[i][1])
        else:
            print(L, R)
            L = LR[i][0]
            R = LR[i][1]
    print(L, R)
