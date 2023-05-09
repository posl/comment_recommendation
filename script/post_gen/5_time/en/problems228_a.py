Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    s, t, x = map(int, input().split())
    if s < t:
        if s < x and x < t:
            print('Yes')
        else:
            print('No')
    else:
        if s < x or x < t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    S, T, X = map(int, input().split())
    if S < T:
        if S < X and X < T:
            print('Yes')
        else:
            print('No')
    else:
        if S < X or X < T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def problem():
    s, t, x = input().split()
    s = int(s)
    t = int(t)
    x = int(x)
    if s < t:
        if s < x and x < t:
            print('Yes')
        else:
            print('No')
    else:
        if s < x or x < t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    s, t, x = map(int, input().split())
    print("Yes" if s <= x <= t else "No")

=======
Suggestion 6

def main():
    S,T,X = map(int,input().split())
    if S <= X and X < T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def problem():
    s,t,x = map(int,input().split())
    if s < t:
        if s < x and x < t:
            print("Yes")
        else:
            print("No")
    else:
        if x > s or x < t:
            print("Yes")
        else:
            print("No")

problem()

=======
Suggestion 8

def main():
    s, t, x = map(int, input().split())
    print("Yes" if (s <= x <= t) else "No")
