def cal(X,Y):
    if (Y-2*X)%2 == 0:
        A = (Y-2*X)/2
        B = X-A
        if A >= 0 and B >= 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
