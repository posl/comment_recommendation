Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, x = map(int, input().split())
    if x < a:
        print(0)
    elif x < a + c:
        print(1)
    elif x <= b:
        print(c / (b - a + 1))
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b, c, x = map(int, input().split())
    if x < a:
        print(0)
    elif x >= a and x <= b:
        print(c / (b - a + 1))
    else:
        print(1)

=======
Suggestion 3

def main():
    A, B, C, X = map(int, input().split())
    if X < A:
        print(0)
    elif X < A + C:
        print(1)
    elif X <= B:
        print(C / (B - A + 1))
    else:
        print(0)

=======
Suggestion 4

def main():
    A,B,C,X = map(int,input().split())
    if X < A:
        print(0)
    elif A <= X <= B:
        print((C/(B-A+1)))
    else:
        print(1)

=======
Suggestion 5

def main():
    A, B, C, X = map(int, input().split())
    print((A <= X <= B) * (C / (B - A + 1)))

main()

=======
Suggestion 6

def main():
    a, b, c, x = map(int, input().split())
    t = 0
    if x <= a:
        t = 1
    elif a < x <= b:
        t = ((b - x + 1) / (b - a + 1)) * ((c - 1) / (b - a))
    print(t)

=======
Suggestion 7

def main():
    A, B, C, X = map(int, input().split())
    ans = 0
    ans += (X >= A) * (1 - (B - X) / (B - A))
    ans += (X >= A + 1) * (C / (B - A))
    print(ans)

=======
Suggestion 8

def main():
    a,b,c,x=map(int,input().split())
    if x<a:
        print(0)
    elif x<=b:
        print(1)
    else:
        print(1-(b-x)/(b-a))

=======
Suggestion 9

def main():
    #input
    A,B,C,X = map(int,input().split())
    #compute
    if X<A:
        ans = 0
    elif A<=X and X<=B:
        ans = (C/(B-A))
    else:
        ans = 1
    #output
    print(ans)

=======
Suggestion 10

def get_input():
    return map(int, input().split())

A, B, C, X = get_input()
