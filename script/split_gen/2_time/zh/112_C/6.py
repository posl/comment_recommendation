def isCenter(x,y,h):
    for i in range(101):
        for j in range(101):
            if h != 0:
                if h == max(h-abs(x-i)-abs(y-j),0):
                    return i,j,h
            else:
                if h == max(h-abs(x-i)-abs(y-j),0):
                    return i,j,h
N = int(input())
p = []
for i in range(N):
    p.append(list(map(int,input().split())))
for i in range(N):
    if p[i][2] != 0:
        x,y,h = p[i][0],p[i][1],p[i][2]
        break
for i in range(101):
    for j in range(101):
        if h != 0:
            if h == max(h-abs(x-i)-abs(y-j),0):
                print(i,j,h)
        else:
            if h == max(h-abs(x-i)-abs(y-j),0):
                print(i,j,h)
