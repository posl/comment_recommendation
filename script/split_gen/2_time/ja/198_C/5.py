def solve():
    R,X,Y = map(int,input().split())
    if (X**2+Y**2)**0.5 == R:
        print(1)
        return
    if (X**2+Y**2)**0.5 <= 2*R:
        print(2)
        return
    print(int((X**2+Y**2)**0.5//R)+1)
