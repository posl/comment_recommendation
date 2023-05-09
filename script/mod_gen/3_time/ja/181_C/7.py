def chk(a,b,c):
    x1 = a[0]
    x2 = b[0]
    x3 = c[0]
    y1 = a[1]
    y2 = b[1]
    y3 = c[1]
    if (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
        return True
    else:
        return False
n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if chk(xy[i],xy[j],xy[k]):
                print("Yes")
                exit()
print("No")

if __name__ == '__main__':
    chk()