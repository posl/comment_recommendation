def main():
    N = int(input())
    XY = []
    for i in range(N):
        XY.append(list(map(int, input().split())))
    S = input()
    if S.count("L") == 0 or S.count("R") == 0:
        print("No")
        return
    for i in range(N):
        if S[i] == "L":
            for j in range(i):
                if S[j] == "R" and XY[i][1] == XY[j][1] and XY[i][0] < XY[j][0]:
                    print("Yes")
                    return
        else:
            for j in range(i + 1, N):
                if S[j] == "L" and XY[i][1] == XY[j][1] and XY[i][0] > XY[j][0]:
                    print("Yes")
                    return
    print("No")
