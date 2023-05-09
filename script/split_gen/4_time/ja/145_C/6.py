def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append([x,y])
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += ((XY[i][0]-XY[j][0])**2 + (XY[i][1]-XY[j][1])**2)**0.5
    ans /= N
    print(ans)
