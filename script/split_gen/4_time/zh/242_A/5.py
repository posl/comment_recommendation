def problems242_a():
    A,B,C,X=map(int,input().split())
    if X<A:
        print(0)
    elif X>=A and X<=B:
        print(1)
    else:
        print(C/(B-A))
