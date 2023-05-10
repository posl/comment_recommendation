def check():
    x,y = map(int,input().split())
    if x == 1 or x == 2:
        if y == 2 or y == 4:
            print("Yes")
        else:
            print("No")
    else:
        if y == 2*x or y == 4*x:
            print("Yes")
        else:
            print("No")
