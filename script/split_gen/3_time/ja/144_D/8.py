def main():
    a,b,x=map(int,input().split())
    if x/a**2<=b/2:
        print(degrees(atan(2*x/a**3)))
    else:
        print(degrees(atan(2*b/a-x/a**2)))
