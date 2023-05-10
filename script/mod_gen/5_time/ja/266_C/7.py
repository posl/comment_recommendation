def check_convexity(x1,y1,x2,y2,x3,y3,x4,y4):
    if x1 == x2:
        if x3 == x4:
            return "No"
        else:
            return "Yes"
    elif x3 == x4:
        return "Yes"
    else:
        a = (y2-y1)/(x2-x1)
        b = y1 - a*x1
        c = (y4-y3)/(x4-x3)
        d = y3 - c*x3
        if a == c and b == d:
            return "No"
        else:
            return "Yes"
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
x4,y4 = map(int,input().split())
print(check_convexity(x1,y1,x2,y2,x3,y3,x4,y4))

if __name__ == '__main__':
    check_convexity()