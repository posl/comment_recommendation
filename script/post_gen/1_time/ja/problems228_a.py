Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S, T, X = map(int, input().split())
    if S < T:
        if S <= X and X < T:
            print("Yes")
        else:
            print("No")
    else:
        if S <= X or X < T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    S, T, X = map(int, input().split())
    if S < T:
        if S <= X < T:
            print("Yes")
        else:
            print("No")
    else:
        if S <= X or X < T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    S, T, X = map(int, input().split())
    if S < T:
        if S <= X < T:
            print("Yes")
        else:
            print("No")
    else:
        if 0 <= X < T or S <= X < 24:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    S, T, X = map(int, input().split())
    if S <= X < T:
        print("Yes")
    elif S > T and (X >= S or X < T):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s, t, x = map(int, input().split())
    if s <= x and x < t:
        print("Yes")
    elif s > t and x < t:
        print("Yes")
    elif s > t and s <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s, t, x = map(int, input().split())
    if s <= x < t:
        print("Yes")
    elif s > t and x >= s:
        print("Yes")
    elif s > t and x < t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    S, T, X = map(int, input().split())
    if X < S:
        print('No')
    elif X >= T:
        print('No')
    else:
        print('Yes')
