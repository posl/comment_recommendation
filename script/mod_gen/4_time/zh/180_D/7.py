def solve(x,y,a,b):
    exp = 0
    while True:
        if x*a <= x+b and x*a < y:
            x *= a
            exp += 1
        else:
            break
    exp += (y-x-1)//b
    return exp
x,y,a,b = map(int,input().split())
print(solve(x,y,a,b))
