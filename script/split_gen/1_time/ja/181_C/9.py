def check_line(x1,y1,x2,y2,x3,y3):
    #print("check_line")
    #print(x1,y1,x2,y2,x3,y3)
    #print((y2-y1)*(x3-x2))
    #print((y3-y2)*(x2-x1))
    if (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
        return True
    else:
        return False
n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i],y[i] = map(int,input().split())
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if check_line(x[i],y[i],x[j],y[j],x[k],y[k]):
                print("Yes")
                exit()
print("No")
