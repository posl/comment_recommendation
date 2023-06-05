def main():
    N = int(input())
    points = []
    for i in range(N):
        x,y = map(int,input().split())
        points.append((x,y))
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if points[i][0] == points[j][0]:
                    if points[i][0] == points[k][0]:
                        print('Yes')
                        return
                elif points[i][1] == points[j][1]:
                    if points[i][1] == points[k][1]:
                        print('Yes')
                        return
                else:
                    if (points[i][0]-points[j][0])*(points[i][1]-points[k][1]) == (points[i][0]-points[k][0])*(points[i][1]-points[j][1]):
                        print('Yes')
                        return
    print('No')
main()
