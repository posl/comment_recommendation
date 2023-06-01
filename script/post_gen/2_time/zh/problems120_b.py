Synthesizing 10/10 solutions

=======
Suggestion 1

def problems120_a():
    A, B, C = map(int, input().split())
    print(min(B // A, C))

=======
Suggestion 2

def main():
    # 读取输入
    a, b, c = map(int, input().split())

    # 计算结果
    result = min(b // a, c)

    # 输出结果
    print(result)

=======
Suggestion 3

def main():
    A,B,C = map(int,input().split())
    if A > C:
        print(0)
    else:
        print(B//A)

=======
Suggestion 4

def solve():
    a,b,c = map(int,input().split())
    print(min(b//a,c))

=======
Suggestion 5

def problem120_a():
    a, b, c = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b // a if c > b // a else c)

problem120_a()

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    print(min(b//a, c))

=======
Suggestion 7

def main():
    # 读入数据
    a, b, c = map(int, input().split())

    # 解决问题
    if a * c <= b:
        ans = c
    else:
        ans = b // a

    # 输出结果
    print(ans)

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    print(min(b//a,c))
main()

=======
Suggestion 9

def solve(a, b, c):
    if a * c <= b:
        return c
    else:
        return b // a

=======
Suggestion 10

def main():
    a, b, c = map(int, input().split())
    print(min(c, b // a))
