Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s, t, x = map(int, input().split())

    if s < t:
        if s < x <= t:
            print('Yes')
        else:
            print('No')
    else:
        if s < x or x <= t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    s, t, x = map(int, input().split())
    if s < t:
        if s <= x and x <= t:
            print("Yes")
        else:
            print("No")
    else:
        if s <= x or x <= t:
            print("Yes")
        else:
            print("No")

main()

=======
Suggestion 3

def main():
    S,T,X = map(int,input().split())
    if S < T:
        if S < X < T:
            print("Yes")
        else:
            print("No")
    else:
        if S < X or X < T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def f():
    s,t,x = map(int, input().split())
    if s < t:
        if s <= x and x <= t:
            print('Yes')
        else:
            print('No')
    else:
        if x <= t or s <= x:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    s,t,x = map(int,input().split())
    if s<t:
        if s<x and x<t:
            print("Yes")
        else:
            print("No")
    elif s>t:
        if x>s or x<t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    s, t, x = map(int, input().split())
    if s < t:
        if s < x and x < t:
            print("Yes")
        else:
            print("No")
    else:
        if s < x or x < t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    S, T, X = map(int, input().split())
    if S < T:
        if S <= X and X < T:
            print('Yes')
        else:
            print('No')
    else:
        if S <= X or X < T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    s,t,x = map(int,input().split())
    if t > s:
        if x >= s and x <= t:
            print('Yes')
        else:
            print('No')
    else:
        if x >= s or x <= t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    s,t,x = map(int,input().split())
    if s < t:
        if s <= x and x < t:
            print("Yes")
        else:
            print("No")
    else:
        if s <= x or x < t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def problem228a(s,t,x):
    if s<t:
        if s<x and x<t:
            print('Yes')
        else:
            print('No')
    else:
        if s<x or x<t:
            print('Yes')
        else:
            print('No')
