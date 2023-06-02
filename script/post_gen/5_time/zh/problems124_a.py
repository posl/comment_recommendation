Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    line = input().split()
    # 转换为整数
    a = int(line[0])
    b = int(line[1])
    # 求最大值
    if a > b:
        print(a + max(a - 1, b))
    else:
        print(b + max(a, b - 1))

=======
Suggestion 2

def solve(a, b):
    if a > b:
        return a + (a - 1)
    elif a < b:
        return b + (b - 1)
    else:
        return a + b

=======
Suggestion 3

def solve(a, b):
    return max(a + a - 1, a + b, b + b - 1)

=======
Suggestion 4

def get_max_coin(a, b):
    if a >= b:
        return a + a - 1
    else:
        return b + b - 1

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(max(a + a - 1, b + b - 1, a + b))

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(max(a+a-1, a+b, b+b-1))

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    if A > B:
        print(A + (A - 1))
    elif A < B:
        print(B + (B - 1))
    else:
        print(A + B)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a == b:
        print(a + b)
    else:
        print(max(a, b) * 2 - 1)

=======
Suggestion 9

def problem124a():
    a,b = map(int,input().split())
    if a == b:
        print(a+b)
    elif a > b:
        print(a+a-1)
    else:
        print(b+b-1)

=======
Suggestion 10

def main():
    A,B = map(int,input().split())
    if A >= B:
        print(A+A-1)
    else:
        print(B+B-1)
