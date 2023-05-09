def check90deg(x1,y1,x2,y2,x3,y3):
    if (x1 == x2 and x2 == x3) or (y1 == y2 and y2 == y3):
        return False
    if x1 == x2:
        if y1 == y3:
            return True
        else:
            return False
    if x2 == x3:
        if y1 == y2:
            return True
        else:
            return False
    if x1 == x3:
        if y1 == y2:
            return True
        else:
            return False
    if y1 == y2:
        if x1 == x3:
            return True
        else:
            return False
    if y2 == y3:
        if x1 == x2:
            return True
        else:
            return False
    if y1 == y3:
        if x1 == x2:
            return True
        else:
            return False
    if abs((y2-y1)/(x2-x1)) == abs((y3-y2)/(x3-x2)):
        return True
    else:
        return False
        
N,x,y = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N-1):
    if check90deg(0,0,A[i],0,A[i+1],0) == False:
        print("No")
        exit()

if __name__ == '__main__':
    check90deg()