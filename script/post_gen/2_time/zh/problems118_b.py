Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    input_str = input("请输入两个数，以空格分隔:")
    input_list = input_str.split(" ")
    return input_list

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)

main()

=======
Suggestion 4

def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算
    if b % a == 0:
        result = a + b
    else:
        result = b - a
    # 输出结果
    print(result)

=======
Suggestion 5

def add_or_sub(a,b):
    if b%a == 0:
        print(a+b)
    else:
        print(b-a)

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if B % A == 0:
        print(A+B)
    else:
        print(B-A)
