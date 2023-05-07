def f(A,B):
    #print("A: {}, B: {}".format(A,B))
    if A==B:
        return A
    elif A==0:
        return f(1,B)
    elif A%2==0:
        return f(A+1,B)
    elif B%2==0:
        return f(A,B-1)
    else:
        return f(A+1,B-1)
