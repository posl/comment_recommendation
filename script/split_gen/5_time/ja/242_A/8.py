def solve():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1.0)
    elif A < X <= B:
        p = (B-X)/(B-A)
        print(p)
    else:
        print(0.0)
