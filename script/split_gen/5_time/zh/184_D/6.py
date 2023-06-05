def solve(a,b,c):
    if a == 0 and b == 0 and c == 0:
        return 0
    return a/(a+b+c)*(1+solve(a+1,b-1,c))+b/(a+b+c)*(1+solve(a,b+1,c-1))+c/(a+b+c)*(1+solve(a,b,c+1))
