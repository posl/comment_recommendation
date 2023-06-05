Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a > b:
        if a > c:
            print(a + max(b, c))
        else:
            print(c + b)
    else:
        if b > c:
            print(b + max(a, c))
        else:
            print(a + c)

=======
Suggestion 2

def problem207_a():
    #读取输入
    a,b,c = map(int,input().split())
    #计算输出
    print(max(a+b,b+c,c+a))

problem207_a()

=======
Suggestion 3

def main():
    # 读入数据
    a, b, c = map(int, input().split())
    # 计算答案
    ans = a + b + c - min(a, b, c)
    # 打印答案
    print(ans)

=======
Suggestion 4

def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b

=======
Suggestion 5

def main():
    a,b,c=map(int,input().split())
    print(max(a+b,b+c,c+a))

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    print(a+b+c-max(a,b,c))

=======
Suggestion 7

def main():
    # 读入数据
    a, b, c = map(int, input().split())
    # 处理数据
    max_num = max(a, b, c)
    # 输出结果
    print(max_num*2 + a + b + c - max_num*3)

=======
Suggestion 8

def main():
    A,B,C = map(int, input().split())
    print(max(A+B,A+C,B+C))

=======
Suggestion 9

def main():
    # 读取输入
    a, b, c = map(int, input().split())

    # 计算答案
    ans = max(a + b, b + c, c + a)

    # 打印答案
    print(ans)

=======
Suggestion 10

def main():
    a, b, c = map(int, input().split())
    print(max(a+b, a+c, b+c))
