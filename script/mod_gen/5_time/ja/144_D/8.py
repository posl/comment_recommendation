def solve(a,b,x):
    if x*2 <= a*a*b:
        return 90 - math.degrees(math.atan(x*2/(a*b*b)))
    else:
        return math.degrees(math.atan((a*a*b-x)*2/(a*a*a)))
import math
a,b,x = map(int,input().split())
print(solve(a,b,x))

if __name__ == '__main__':
    solve()