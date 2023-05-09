def check_line(a,b,c):
    if (a[0] == b[0] and b[0] == c[0]) or (a[1] == b[1] and b[1] == c[1]):
        return True
    elif (a[1] - b[1]) / (a[0] - b[0]) == (b[1] - c[1]) / (b[0] - c[0]):
        return True
    else:
        return False
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split())))
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if check_line(points[i],points[j],points[k]):
                print("Yes")
                exit()
print("No")
