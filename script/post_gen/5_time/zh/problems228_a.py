Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    s, t, x = map(int, input().split())
    if s < t:
        if s <= x < t:
            print("Yes")
        else:
            print("No")
    else:
        if s <= x or x < t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def is_light(s, t, x):
    if s < t:
        return s <= x and x < t
    else:
        return s <= x or x < t

=======
Suggestion 4

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
Suggestion 7

def get_input():
    """获取输入数据"""
    line = input()
    return line.split()

=======
Suggestion 8

def main():
    s,t,x = map(int,input().split())
    if (s<t):
        if (s<x) and (x<t):
            print("Yes")
        else:
            print("No")
    else:
        if (s<x) or (x<t):
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    S,T,X = map(int,input().split())
    if S<T:
        if S<=X and X<T:
            print('Yes')
        else:
            print('No')
    else:
        if S<=X or X<T:
            print('Yes')
        else:
            print('No')
