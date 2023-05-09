Synthesizing 10/10 solutions

=======
Suggestion 1

def allowance(a, b, c):
    return max(a * 10 + b + c, a + b * 10 + c, a + b + c * 10)

=======
Suggestion 2

def main():
    a,b,c = map(int, input().split())
    print(max(a*10+b+c, a+b*10+c, a+b+c*10))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a+b*10+c, a+b+c*10))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(max(A+B, A+C, B+C))

=======
Suggestion 5

def allowance(a,b,c):
    if a==b==c:
        return 111*a
    elif a==b or b==c or a==c:
        return 111*max(a,b,c)
    else:
        return 111*min(a,b,c)+100*max(a,b,c)

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    print(max([a+b+c, a+b-c, a-b+c, a-b-c]))

=======
Suggestion 7

def allowance():
    allowance = 0
    a, b, c = input().split()
    if a == b == c:
        allowance = int(a + b + c) * 3
    elif a == b:
        allowance = int(a + b) * 2 + int(c)
    elif a == c:
        allowance = int(a + c) * 2 + int(b)
    elif b == c:
        allowance = int(b + c) * 2 + int(a)
    else:
        allowance = int(a) + int(b) + int(c)
    print(allowance)

allowance()

=======
Suggestion 8

def allowance():
    A, B, C = map(int, input().split())
    print(max(A+B, A+C, B+C))

=======
Suggestion 9

def problem():
    a = input()
    b = input()
    c = input()
    print(int(a)+int(b)+int(c))
problem()

=======
Suggestion 10

def get_input():
    return map(int, input().split())
