Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    #print(a, b, c)
    if a > c:
        print(0)
        return
    print(b//a if b//a < c else c)

main()

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if a*c <= b:
        print(c)
    else:
        print(b//a)

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if a <= b:
        print(c//a)
    else:
        print(b//a)

=======
Suggestion 4

def solve():
    a,b,c = map(int,input().split())
    if a > b:
        print(0)
    else:
        print(b // a if b // a < c else c)

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if a * c > b:
        print(b // a)
    else:
        print(c)

=======
Suggestion 6

def solve():
    a,b,c = map(int,input().split())
    if b >= a*c:
        print(c)
    else:
        print(b//a)

=======
Suggestion 7

def solve(a, b, c):
    # 你的代码
    return min(b//a, c)

=======
Suggestion 8

def problem120_a():

    # 读取输入
    a, b, c = map(int, input().split())

    # 计算结果
    result = min(b//a, c)

    # 输出结果
    print(result)

=======
Suggestion 9

def problem120_a():
    a, b, c = map(int, input().split())
    print(min(b // a, c))


problem120_a()

=======
Suggestion 10

def main():
    # 读入数据
    a,b,c = map(int, input().split())
    ans = min(b//a, c)
    print(ans)
