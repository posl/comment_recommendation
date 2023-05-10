Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X < Y:
        if X * A < X + B:
            X *= A
            exp += 1
        else:
            exp += (Y - X - 1) // B
            break
    print(exp)

=======
Suggestion 2

def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
            exp += 1
        else:
            exp += (y - x - 1) // b
            break
    print(exp)

=======
Suggestion 3

def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
            exp += 1
        else:
            x += b
            exp += 1
    print(exp - 1)

=======
Suggestion 4

def main():
    x, y, a, b = map(int, input().split())
    cnt = 0
    while a*x < x+b and a*x < y:
        x *= a
        cnt += 1
    cnt += (y-1-x)//b
    print(cnt)

=======
Suggestion 5

def main():
    # input
    x, y, a, b = map(int, input().split())

    # compute
    exp = 0
    while x*a < x+b and x*a < y:
        x *= a
        exp += 1
    exp += (y-x-1)//b

    # output
    print(exp)

=======
Suggestion 6

def solve(x, y, a, b):
    exp = 0
    while True:
        if x*a >= y:
            break
        if x*a < x+b:
            exp += 1
            x *= a
        else:
            exp += (y-x)//b
            break
    return exp

=======
Suggestion 7

def main():
    x, y, a, b = map(int, input().split())
    ans = 0
    while x < y:
        if x * a < x + b:
            x *= a
        else:
            x += b
        ans += 1
    print(ans - 1)

=======
Suggestion 8

def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
            exp += 1
        else:
            if (y - x) % b == 0:
                exp += (y - x) // b - 1
                break
            else:
                exp += (y - x) // b
                break
    print(exp)

=======
Suggestion 9

def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X < Y:
        if X*A < X+B:
            X *= A
            exp += 1
        else:
            X += B
            exp += 1
    print(exp-1)

=======
Suggestion 10

def train(x,y,a,b):
    exp=0
    while True:
        if x*a>=y:
            break
        else:
            exp+=1
            x*=a
    exp+=(y-x)//b
    if (y-x)%b!=0:
        exp+=1
    return exp

x,y,a,b=map(int,input().split())
print(train(x,y,a,b))
