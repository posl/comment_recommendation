def problems242_a():
    A,B,C,X = map(int,input().split())
    if X<=A:
        print(1.0)
    elif X>A and X<B:
        print(C/(B-A))
    else:
        print(0.0)
