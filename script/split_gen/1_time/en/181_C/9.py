def check_if_on_line(x1,y1,x2,y2,x3,y3):
    return (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2)
N = int(input())
points = [list(map(int,input().split())) for i in range(N)]
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if check_if_on_line(points[i][0],points[i][1],points[j][0],points[j][1],points[k][0],points[k][1]):
                print('Yes')
                exit()
print('No')
