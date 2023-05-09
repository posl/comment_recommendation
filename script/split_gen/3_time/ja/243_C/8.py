def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    for i in range(N):
        for j in range(i + 1, N):
            if XY[i][1] == XY[j][1] and XY[i][0] < XY[j][0]:
                if S[i] == "R" and S[j] == "L":
                    print("Yes")
                    return
    print("No")
