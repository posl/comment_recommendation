Synthesizing 10/10 solutions

=======
Suggestion 1

def solution():
    x,y,a,b = map(int,input().split())
    if a == 1:
        if y - x > b:
            print(y - x - 1)
        else:
            print(0)
    else:
        ans = 0
        while x < y:
            if x * a < x + b:
                x *= a
            else:
                x += b
            ans += 1
        print(ans - 1)

=======
Suggestion 2

def main():
    x,y,a,b = map(int,input().split())
    exp = 0
    while x*a <= x+b and x*a < y:
        x *= a
        exp += 1
    print(exp + (y-x-1)//b)

=======
Suggestion 3

def solve(x,y,a,b):
    if x>=y:
        return 0
    if b>=a:
        return (y-x-1)//a
    else:
        if (x*b)%a==0:
            return max((y-x-1)//a,(y-x-1)//a*(x*b)//a)
        else:
            return max((y-x-1)//a,(y-x-1)//a*(x*b)//a,(y-x-1)//a*(x*b)//a+1)

=======
Suggestion 4

def train(x, y, a, b):
    exp = 0
    while True:
        if x * a < x + b:
            if x * a >= y:
                return exp
            else:
                x *= a
                exp += 1
        else:
            if x + b >= y:
                return exp
            else:
                x += b
                exp += 1

=======
Suggestion 5

def solve(x,y,a,b):
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
            exp += 1
        else:
            x += b
            exp += 1
    return exp

=======
Suggestion 6

def solve(X,Y,A,B):
    exp=0
    while X*A<X+B and X*A<Y:
        X*=A
        exp+=1
    exp+=(Y-X-1)//B
    return exp

=======
Suggestion 7

def solve(x, y, a, b):
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
        else:
            x += b
        exp += 1
    return exp

=======
Suggestion 8

def problems180_d():
    x, y, a, b = map(int, input().split())
    exp = 0
    while True:
        if x * a <= x + b and x * a < y:
            x *= a
            exp += 1
        else:
            if x + b < y:
                x += b
                exp += 1
            else:
                break
    print(exp)

=======
Suggestion 9

def main():
    x,y,a,b=map(int,input().split())
    exp=0
    while x<a*x and x<a*x+b and x<a*x+b<y:
        x*=a
        exp+=1
    exp+=(y-x-1)//b
    print(exp)

=======
Suggestion 10

def solve(x, y, a, b):
    exp = 0
    while x * a <= x + b and x * a < y:
        x *= a
        exp += 1
    exp += (y - 1 - x) // b
    return exp

x, y, a, b = map(int, input().split())
print(solve(x, y, a, b))
