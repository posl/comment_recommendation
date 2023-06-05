def getTshirt():
    A,B,C,X = map(int,input().split())
    if X <= A:
        return 1.0
    elif X <= B:
        return C/(B-A)
    else:
        return 0.0
print(getTshirt())
