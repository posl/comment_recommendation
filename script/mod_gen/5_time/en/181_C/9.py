def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    #print(points)
    if N == 3:
        print("Yes")
        return
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                #print(points[i], points[j], points[k])
                if (points[j][0] - points[i][0]) * (points[k][1] - points[i][1]) == (points[k][0] - points[i][0]) * (points[j][1] - points[i][1]):
                    print("Yes")
                    return
    print("No")
    return

if __name__ == '__main__':
    main()