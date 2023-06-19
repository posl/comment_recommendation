def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append((x, y))
    #print(XY)
    max = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(i, j)
            #print(XY[i], XY[j])
            d = ((XY[i][0]-XY[j][0])**2 + (XY[i][1]-XY[j][1])**2)**0.5
            #print(d)
            if d > max:
                max = d
    print(max)
main()
