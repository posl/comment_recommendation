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
    S, T, X = map(int, input().split())
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
Suggestion 3

def main():
    s, t, x = map(int, input().split())
    if s <= t:
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
Suggestion 4

def main():
    s, t, x = map(int, input().split())
    if (s < t):
        if (s < x and x < t):
            print("Yes")
        else:
            print("No")
    elif (t < s):
        if (s < x or x < t):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 5

def main():
    s, t, x = map(int, input().split())
    if s < t:
        print('Yes' if s <= x and t > x else 'No')
    else:
        print('Yes' if s <= x or t > x else 'No')

=======
Suggestion 6

def main():
    s, t, x = map(int, input().split())
    if (s <= x and x < t):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def is_light_on(s, t, x):
    if s < t:
        return s < x and x < t
    else:
        return s < x or x < t

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    if (a < b):
        if (a < c and c <= b):
            print("Yes")
        else:
            print("No")
    else:
        if (a < c or c <= b):
            print("Yes")
        else:
            print("No")
main()
