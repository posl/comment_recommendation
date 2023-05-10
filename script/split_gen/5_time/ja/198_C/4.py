def solve():
    R, X, Y = map(int, input().split())
    if X*X + Y*Y < R*R:
        print(2)
    else:
        print((X*X+Y*Y)**(1/2)//R + (1 if (X*X+Y*Y)**(1/2)%R != 0 else 0))
