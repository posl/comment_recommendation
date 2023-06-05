def solve(x,y,a,b):
    exp=0
    if x>=y:
        return exp
    else:
        while x<y:
            if x*a<x+b:
                x=x*a
                exp+=1
            else:
                x=x+b
                exp+=1
        return exp
