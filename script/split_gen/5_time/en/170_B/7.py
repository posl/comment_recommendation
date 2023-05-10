def solve(X,Y):
    if Y%2 == 0:
        if 2*X <= Y <= 4*X:
            return "Yes"
        else:
            return "No"
    else:
        return "No"
X,Y = map(int,input().split())
print(solve(X,Y))
