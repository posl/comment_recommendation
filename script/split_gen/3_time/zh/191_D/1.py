def count(x,y,r):
    count = 0
    for i in range(int(x-r),int(x+r)+1):
        for j in range(int(y-r),int(y+r)+1):
            if (x-i)**2 + (y-j)**2 <= r**2:
                count += 1
    return count
x,y,r = map(float,input().split())
print(count(x,y,r))
