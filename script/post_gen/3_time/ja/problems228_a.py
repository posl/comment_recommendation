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
    s, t, x = map(int, input().split())
    if s <= x and x < t:
        print("Yes")
    elif s > t and (x >= s or x < t):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s,t,x = map(int,input().split())
    if s < t:
        if s <= x <= t:
            print("Yes")
        else:
            print("No")
    else:
        if 0 <= x <= t:
            print("Yes")
        elif s <= x <= 23:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print("Yes")
    elif S == 23 and T == 0 and X == 23:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s, t, x = map(int, input().split())
    if x < s:
        print("No")
    elif x >= t:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    #入力
    s, t, x = map(int, input().split())
    #出力
    print('Yes' if s <= x < t else 'No')
