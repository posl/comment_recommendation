def rsp(x,y):
    if x == 0:
        if y == 0:
            return 0
        elif y == 1:
            return 2
        else:
            return 1
    elif x == 1:
        if y == 0:
            return 1
        elif y == 1:
            return 0
        else:
            return 2
    else:
        if y == 0:
            return 2
        elif y == 1:
            return 1
        else:
            return 0
x,y = map(int,input().split())
print(rsp(x,y))
