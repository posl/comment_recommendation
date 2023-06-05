def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(input().split())
    points.sort()
    #print(points)
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if (int(points[i][0])-int(points[j][0]))*(int(points[j][1])-int(points[k][1])) == (int(points[i][1])-int(points[j][1]))*(int(points[j][0])-int(points[k][0])):
                    print('Yes')
                    return
    print('No')
    return
main()
