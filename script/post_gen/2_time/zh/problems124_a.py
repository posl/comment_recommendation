Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    print(max(a+a-1, a+b, b+b-1))

=======
Suggestion 2

def problems124_a():
    # 读取两个整数
    A, B = map(int, input().split())
    # 用列表存储两个按钮的值
    list = [A, B]
    # 用列表存储按两次按钮的结果
    list2 = []
    # 用for循环遍历两个按钮的值
    for i in range(len(list)):
        # 用while循环计算按两次按钮的结果
        while list[i] > 0:
            # 按两次按钮的结果
            list2.append(list[i])
            # 按一次按钮的结果
            list[i] -= 1
    # 输出按两次按钮的结果之和
    print(sum(list2))

problems124_a()

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    if a == b:
        print(a + b)
    else:
        print(max(a,b)*2-1)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print(max(A + A - 1, A + B, B + B - 1))

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if a > b:
        print(a+a-1)
    elif a < b:
        print(b+b-1)
    else:
        print(a+b)

=======
Suggestion 6

def problem124_a():
    a,b = map(int,input().split())
    if a == b:
        print(a+a)
    elif a > b:
        print(a+a-1)
    else:
        print(b+b-1)

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    if A == B:
        print(2*A)
    elif A > B:
        print(2*A-1)
    else:
        print(2*B-1)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a <= b:
        print(b + max(b - 1, a))
    else:
        print(a + max(a - 1, b))
