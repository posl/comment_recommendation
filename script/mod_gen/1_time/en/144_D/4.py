def solve(a,b,x):
    if x <= a*a*b/2:
        return math.degrees(math.atan(2*x/(a*a*b)))
    else:
        return math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))
a,b,x = map(int,input().split())
print(solve(a,b,x))
import math
a,b,x = map(int,input().split())

if __name__ == '__main__':
    solve()