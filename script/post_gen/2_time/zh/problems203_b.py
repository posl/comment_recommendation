Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif a == c:
        print(b)
    else:
        print(0)

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)

=======
Suggestion 3

def get_input():
    a, b, c = map(int, input().split())
    return a, b, c

=======
Suggestion 4

def main():
    a,b,c = input().split()
    if a==b:
        print(c)
    elif a==c:
        print(b)
    elif b==c:
        print(a)
    else:
        print(0)

=======
Suggestion 5

def dice_game(a,b,c):
    if a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return 0

=======
Suggestion 6

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 逻辑处理
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    if a==b:
        print(c)
    elif b==c:
        print(a)
    elif c==a:
        print(b)
    else:
        print(0)
