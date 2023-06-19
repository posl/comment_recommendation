def main():
    X,Y=map(int,input().split())
    if (X+Y)%3!=0:
        print(0)
        return
    if 2*X-Y<0 or 2*Y-X<0:
        print(0)
        return
    a=(2*X-Y)//3
    b=(2*Y-X)//3
    if a+b!=X:
        print(0)
        return
    print(combination(a,b))
