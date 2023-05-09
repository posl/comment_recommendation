def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    #print(points)
    
    #x座標の差が同じものを探す
    x_diff = []
    for i in range(N):
        for j in range(i+1, N):
            x_diff.append(points[j][0] - points[i][0])
    x_diff.sort()
    #print(x_diff)
    
    #y座標の差が同じものを探す
    y_diff = []
    for i in range(N):
        for j in range(i+1, N):
            y_diff.append(points[j][1] - points[i][1])
    y_diff.sort()
    #print(y_diff)
    
    #x座標の差が同じものを探す
    x_diff = []
    for i in range(N):
        for j in range(i+1, N):
            x_diff.append(points[j][0] - points[i][0])
    x_diff.sort()
    #print(x_diff)
    
    #x座標の差が同じもののy座標の差が同じものを探す
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(N):
                for l in range(k+1, N):
                    if points[i][0] < points[k][0] and points[k][0] < points[j][0] and points[i][1] < points[l][1] and points[l][1] < points[j][1]:
                        count += 1
    print(count)

if __name__ == '__main__':
    main()