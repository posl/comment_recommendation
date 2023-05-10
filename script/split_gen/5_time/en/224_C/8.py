def main():
    N = int(input())
    XY = []
    for _ in range(N):
        XY.append(list(map(int, input().split())))
    
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1 = XY[i][0]
                y1 = XY[i][1]
                x2 = XY[j][0]
                y2 = XY[j][1]
                x3 = XY[k][0]
                y3 = XY[k][1]
                if (x1-x2)*(y1-y3) != (x1-x3)*(y1-y2):
                    count += 1
    print(count)
