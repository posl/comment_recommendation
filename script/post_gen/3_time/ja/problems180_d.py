Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X < Y:
        if X * A < X + B:
            X *= A
            exp += 1
        else:
            break
    exp += (Y - 1 - X) // B
    print(exp)

=======
Suggestion 3

def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X < Y and X * A < X + B:
        X *= A
        exp += 1
    exp += (Y - X - 1) // B
    print(exp)

=======
Suggestion 4

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
Suggestion 5

def main():
    # input
    X, Y, A, B = map(int, input().split())

    # compute
    cnt = 0
    while X*A <= X+B and X*A < Y:
        X *= A
        cnt += 1
    cnt += (Y-X-1)//B

    # output
    print(cnt)

=======
Suggestion 6

def main():
    x,y,a,b = map(int,input().split())
    cnt = 0
    while x*a < x+b and x*a < y:
        x *= a
        cnt += 1
    cnt += (y-x-1)//b
    print(cnt)

=======
Suggestion 7

def main():
    x,y,a,b = map(int,input().split())
    exp = 0
    while True:
        if x*a < x+b:
            if x*a >= y:
                break
            x *= a
            exp += 1
        else:
            if x+b >= y:
                break
            x += b
            exp += 1
    print(exp)

=======
Suggestion 8

def solve(x, y, a, b):
    exp = 0
    while (a*x) < (x + b) and x < y:
        x *= a
        exp += 1
    exp += (y - x - 1) // b
    return exp

=======
Suggestion 9

def calc_exp(exp, a, b):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return calc_exp(exp/2, a, b)**2 % MOD
    else:
        return calc_exp(exp-1, a, b) * a % MOD
