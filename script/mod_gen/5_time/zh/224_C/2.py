def get_area(x1,y1,x2,y2,x3,y3):
    return abs(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2)/2
n=int(input())
point=[]
for i in range(n):
    point.append(list(map(int,input().split())))
count=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if get_area(point[i][0],point[i][1],point[j][0],point[j][1],point[k][0],point[k][1])!=0:
                count+=1
print(count)

if __name__ == '__main__':
    get_area()