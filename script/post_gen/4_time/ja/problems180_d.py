Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X * A < X + B and X * A < Y:
        X *= A
        exp += 1
    exp += (Y - 1 - X) // B
    print(exp)

=======
Suggestion 2

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
Suggestion 3

def main():
    x, y, a, b = map(int, input().split())
    ans = 0
    while a * x < y and a * x < x + b:
        x *= a
        ans += 1
    ans += (y - 1 - x) // b
    print(ans)
main()

=======
Suggestion 4

def main():
    x,y,a,b = map(int, input().split())
    exp = 0
    while x*a < x+b and x*a < y:
        x *= a
        exp += 1
    exp += (y-x-1)//b
    print(exp)

=======
Suggestion 5

def solve():
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
Suggestion 6

def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while A * X < B + X and A * X < Y:
        X *= A
        exp += 1
    exp += (Y - 1 - X) // B
    print(exp)

=======
Suggestion 7

def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X < Y:
        if X * A >= X + B:
            if X * A >= Y:
                break
            X *= A
            exp += 1
        else:
            if X + B >= Y:
                break
            X += B
            exp += 1
    print(exp)

=======
Suggestion 8

def myCode():
    X,Y,A,B = map(int,input().split())
    cnt = 0
    while X < Y:
        if X * A < X + B:
            X *= A
            cnt += 1
        else:
            cnt += (Y - X - 1) // B
            break
    print(cnt)

=======
Suggestion 9

def solve(x, y, a, b):
    if y <= x:
        return 0

    exp = 0
    while True:
        if x*a < x+b and x*a < y:
            x *= a
            exp += 1
        else:
            exp += (y-x-1)//b
            break
    return exp
