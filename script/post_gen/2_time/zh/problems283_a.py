Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(a ** b)

=======
Suggestion 2

def main():
    print("请输入两个整数，用空格分隔：")
    a, b = map(int, input().split())
    print(a**b)

=======
Suggestion 3

def power(a,b):
    result = 1
    for i in range(b):
        result = result * a
    return result

=======
Suggestion 4

def main():
    # 读取A和B
    A, B = map(int, input().split())

    # 输出A^B
    print(A ** B)
