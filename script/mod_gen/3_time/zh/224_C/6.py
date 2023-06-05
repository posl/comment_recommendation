def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(input().split())
    points.sort(key=lambda x:int(x[0]))
    #print(points)
    count = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if (int(points[j][1])-int(points[i][1]))*(int(points[k][0])-int(points[i][0])) == (int(points[k][1])-int(points[i][1]))*(int(points[j][0])-int(points[i][0])):
                    continue
                else:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()