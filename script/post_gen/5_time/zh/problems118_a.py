Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)

=======
Suggestion 2

def calc(a,b):
    if a%b==0:
        return a+b
    else:
        return b-a

=======
Suggestion 3

def main():
    A,B=map(int,input().split())
    if B%A==0:
        print(A+B)
    else:
        print(B-A)

=======
Suggestion 4

def main():
    # 读取输入
    a,b = map(int,input().split())
    # 判断输出
    if b%a == 0:
        print(a+b)
    else:
        print(b-a)

=======
Suggestion 5

def cal(a,b):
    if b%a == 0:
        return a+b
    else:
        return b-a

=======
Suggestion 6

def get_input():
    A,B = map(int,input().split())
    if 1 <= A <= B <= 20:
        return A,B
    else:
        print("输入不符合要求，请重新输入")
        return get_input()

=======
Suggestion 7

def problems118_a():
    a, b = map(int, input().split())
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)
