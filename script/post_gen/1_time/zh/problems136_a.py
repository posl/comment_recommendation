Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    a, b, c = map(int, input().split())

    # 从瓶子2转移到瓶子1
    if b >= a:
        print(c)
    else:
        print(c - (a - b))

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a >= b + c:
        print(0)
    else:
        print(c - (a - b))

=======
Suggestion 3

def main():
    # 从标准输入读取
    a,b,c = map(int, input().split())
    # 从瓶子2转移到瓶子1
    b = b + c
    # 2号瓶中还有多少水
    c = 0
    # 1号瓶中还可以装多少水
    a = a - b
    # 1号瓶中装满
    if a < 0:
        c = abs(a)
        a = 0
    print(c)

=======
Suggestion 4

def main():
    A,B,C = map(int,input().split())
    print(C-(A-B) if C-(A-B) > 0 else 0)

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if a > b + c:
        print(0)
    else:
        print(c - (a - b))

main()

=======
Suggestion 6

def main():
    # 读取输入
    A, B, C = map(int, input().split())

    # 从2号瓶中尽可能地将水转移到1号瓶
    # 2号瓶中剩余水量
    C -= A - B

    # 输出结果
    print(C if C >= 0 else 0)

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    if b+c<a:
        print(c)
    else:
        print(a-b)

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    print(c - (a - b) if a - b < c else 0)

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if a < b+c:
        print(b+c-a)
    else:
        print(0)

=======
Suggestion 10

def main():
    A,B,C = map(int,input().split())
    print(max(0,C-(A-B)))
