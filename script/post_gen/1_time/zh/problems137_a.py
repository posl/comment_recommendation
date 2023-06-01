Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    print(max(a+b,a-b,a*b))

=======
Suggestion 2

def max(a,b):
    if a>b:
        return a
    else:
        return b

=======
Suggestion 3

def max(a,b):
    if a+b>a-b:
        if a+b>a*b:
            return a+b
        else:
            return a*b
    else:
        if a-b>a*b:
            return a-b
        else:
            return a*b

a,b=map(int,input().split())
print(max(a,b))

=======
Suggestion 4

def main():
    # 读取标准输入
    a, b = map(int, input().split())
    # 计算
    print(max(a + b, a - b, a * b))

=======
Suggestion 5

def max(a,b):
    if a > b:
        return a
    else:
        return b

a,b = map(int,input().split())
print(max(a+b,a-b))
print(max(a+b,a*b))
