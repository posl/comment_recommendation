def main():
    r,x,y = map(int,input().split())
    if 0 == x and 0 == y:
        print(0)
    elif 0 == x or 0 == y:
        print(1)
    else:
        if r*r > x*x + y*y:
            print(2)
        else:
            print(int((x*x+y*y)**0.5/r) + 1)
