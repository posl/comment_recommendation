Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x,y,a,b=map(int,input().split())
    exp=0
    while x*a<=x+b and x*a<y:
        x*=a
        exp+=1
    exp+=(y-1-x)//b
    print(exp)

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
        else:
            x += b
        exp += 1
    print(exp - 1)

=======
Suggestion 4

def solution():
    x,y,a,b = map(int,input().split())
    exp = 0
    while x*a < x+b and x*a<y:
        x *= a
        exp += 1
    exp += (y-1-x)//b
    print(exp)

=======
Suggestion 5

def problem180_d(x,y,a,b):
    exp = 0
    str = x
    while str < y:
        if str*a < str + b:
            str = str * a
            exp += 1
        else:
            str = str + b
            exp += 1
    print(exp)

=======
Suggestion 6

def f(x,y,a,b):
    exp = 0
    str = x
    while str < y:
        if str * a < str + b:
            str = str * a
        else:
            str = str + b
        exp += 1
    return exp

x,y,a,b = map(int, input().split())
print(f(x,y,a,b))

=======
Suggestion 7

def solve():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x * a < x + b and x * a < y:
        x *= a
        exp += 1
    exp += (y - x - 1) // b
    print(exp)

=======
Suggestion 8

def problem180_d():
    x,y,a,b = map(int,input().split())
    i = 0
    while True:
        if x*a < x+b and x*a < y:
            x = x*a
            i += 1
        else:
            break
    i += (y-x-1)//b
    print(i)

=======
Suggestion 9

def solve():
    x, y, a, b = map(int, input().split())
    ans = 0
    while a * x < y and a * x < x + b:
        x *= a
        ans += 1
    ans += (y - 1 - x) // b
    print(ans)

solve()
