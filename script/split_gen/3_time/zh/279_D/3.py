def solve():
    A,B = map(int,input().split())
    if A >= B:
        print(A/2)
    else:
        print((A+B)/2)
