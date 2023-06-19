Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    s, t, x = map(int, input().split())
    if s < t:
        if s <= x and x < t:
            print('Yes')
        else:
            print('No')
    else:
        if s <= x or x < t:
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

def main():
    S,T,X = map(int,input().split())
    if S < T:
        if S < X and X < T:
            print("Yes")
        else:
            print("No")
    else:
        if S < X or X < T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    s, t, x = map(int, input().split())
    if s < t:
        if x > s and x < t:
            print("Yes")
        else:
            print("No")
    else:
        if x > s or x < t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    s,t,x = map(int,input().split())
    if s > t:
        if x >= s or x <= t:
            print("Yes")
        else:
            print("No")
    else:
        if x >= s and x <= t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    s, t, x = map(int, input().split())
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
Suggestion 8

def main():
    s, t, x = [int(i) for i in input().split()]
    if s < t:
        if s <= x and x <= t:
            print("Yes")
        else:
            print("No")
    else:
        if x <= t or s <= x:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    S, T, X = map(int, input().split())
    if S < T:
        if X > S and X < T:
            print('Yes')
        else:
            print('No')
    else:
        if X > S or X < T:
            print('Yes')
        else:
            print('No')
