Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a == b:
        print(str(a) * a)
    elif a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    if a < b:
        print(str(a)*b)
    else:
        print(str(b)*a)

=======
Suggestion 3

def main():
    # 读取输入
    a, b = map(int, input().split())
    # 处理
    a_str = str(a) * b
    b_str = str(b) * a
    # 输出
    if a_str < b_str:
        print(a_str)
    else:
        print(b_str)

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    if a > b:
        print(str(b)*a)
    elif a < b:
        print(str(a)*b)
    else:
        print(str(a)*b)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a <= b:
        print(str(a) * b)
    else:
        print(str(b) * a)


main()

=======
Suggestion 6

def problem152_b():
    a, b = map(int, input().split())
    if a == b:
        print(str(a) * a)
    elif a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)
