Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    a, b, c = map(int, input().split())

    # 处理
    if a * c <= b:
        ans = c
    else:
        ans = b // a

    # 输出结果
    print(ans)

=======
Suggestion 2

def drink_sound():
    a,b,c = map(int,input().split())
    if a>b:
        print(0)
    else:
        print(min(b//a,c))

=======
Suggestion 3

def main():
    #input
    a, b, c = map(int, input().split())
    #calculate
    if a * c <= b:
        ans = c
    else:
        ans = b // a
    #output
    print(ans)

=======
Suggestion 4

def buy_drink(A, B, C):
    if A > B:
        return 0
    else:
        return min(B // A, C)

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(min(b//a,c))

=======
Suggestion 6

def problem120_a():
    a,b,c = map(int,input().split(' '))
    if a * c > b:
        print(b // a)
    else:
        print(c)

=======
Suggestion 7

def problem120_a():
    a,b,c = map(int,input().split())
    if a*c <= b:
        print(c)
    else:
        print(b//a)

=======
Suggestion 8

def problems120_a():
    a, b, c = map(int, input().split())
    if a * c <= b:
        print(c)
    else:
        print(int(b / a))
