def problems239_c():
    x1,y1,x2,y2 = map(int,input().split())
    if (abs(x1-x2)**2 + abs(y1-y2)**2)**(1/2) == (5)**(1/2):
        print("Yes")
    else:
        print("No")
