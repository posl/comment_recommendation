Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    print(min(b//a,c))
    return

=======
Suggestion 2

def problem120_a():
    a,b,c = map(int,input().split())
    if a*c <= b:
        print(c)
    else:
        print(b//a)

=======
Suggestion 3

def problem120_a():
    a,b,c = map(int,input().split())
    print(min(b//a,c))

problem120_a()

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if a*c <= b:
        print(c)
    else:
        print(b//a)

=======
Suggestion 5

def solve():
    a,b,c = map(int,input().split())
    return min(b//a,c)

print(solve())

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
    if (A * C) <= B:
        print(C)
    else:
        print(B // A)

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    print(min(b//a,c))

=======
Suggestion 8

def main():
    a,b,c=map(int,input().split())
    if b//a>=c:
        print(c)
    else:
        print(b//a)

=======
Suggestion 9

def getNum():
    a,b,c = map(int, input().split())
    if b >= a*c:
        return c
    else:
        return b//a

=======
Suggestion 10

def main():
    # 读取输入
    a,b,c = map(int,input().split())
    # 处理
    d = b//a
    if d > c:
        d = c
    # 输出
    print(d)
