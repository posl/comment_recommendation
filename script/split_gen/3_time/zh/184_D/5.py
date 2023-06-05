def solve(a,b,c):
    if a==100 or b==100 or c==100:
        return 0
    return 1+solve(a+1,b,c)*(a/(a+b+c))+solve(a,b+1,c)*(b/(a+b+c))+solve(a,b,c+1)*(c/(a+b+c))
