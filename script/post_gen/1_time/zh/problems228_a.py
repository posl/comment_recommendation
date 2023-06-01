Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s, t, x = map(int, input().split())
    if s <= t:
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
Suggestion 2

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
Suggestion 3

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
Suggestion 4

def main():
    s,t,x = map(int, input().split())
    if s>t:
        if x>=s or x<t:
            print('Yes')
        else:
            print('No')
    else:
        if x>=s and x<t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    s,t,x = map(int,input().split())
    if s < t:
        if s <= x and x <= t:
            print('Yes')
        else:
            print('No')
    else:
        if s <= x or x <= t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def isLight(s, t, x):
    if s < t:
        return s <= x and x < t
    elif s > t:
        return s <= x or x < t
    else:
        return False

s, t, x = map(int, input().split())

=======
Suggestion 7

def problems228_a():
    s,t,x = map(int, input().split())
    if s <= x and x < t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s,t,x = map(int,input().split())
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
Suggestion 9

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
Suggestion 10

def main():
    # 读入数据
    s,t,x = map(int,input().split())
    # 处理数据
    if x > s and x < t:
        print("Yes")
    else:
        print("No")
