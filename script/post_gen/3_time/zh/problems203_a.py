Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 处理
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)
    return 0

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)

=======
Suggestion 5

def main():
    # 读取输入
    a, b, c = map(int, input().split())

    # 解决问题
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)

=======
Suggestion 6

def main():
    # 读入a,b,c
    a,b,c = map(int,input().split())

    # 逻辑处理
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)
