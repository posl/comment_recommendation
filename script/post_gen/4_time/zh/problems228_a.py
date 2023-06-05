Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s,t,x = map(int,input().split())
    if s < t:
        if s < x < t:
            print("Yes")
        else:
            print("No")
    else:
        if s < x or x < t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    s,t,x = map(int,input().split())
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

=======
Suggestion 3

def is_light_on(s, t, x):
    if s < t:
        if s < x and x < t:
            return True
        else:
            return False
    else:
        if t < x and x < s:
            return False
        else:
            return True

=======
Suggestion 4

def main():
    S,T,X=map(int,input().split())
    if S==T:
        print("No")
    elif S<T:
        if S<X and X<T:
            print("Yes")
        else:
            print("No")
    else:
        if S<X or X<T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    s,t,x = map(int,input().split())
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
Suggestion 6

def main():
    s,t,x = map(int,input().split())
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
