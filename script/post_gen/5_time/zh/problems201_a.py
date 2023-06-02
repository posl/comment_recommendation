Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    a = input()
    a = a.split()
    a = [int(i) for i in a]
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def isArithmeticSequence(a1, a2, a3):
    if a3 - a2 == a2 - a1:
        return True
    else:
        return False

a1, a2, a3 = map(int, input().split())

=======
Suggestion 4

def main():
    a1,a2,a3 = map(int,input().split())
    if a3-a2 == a2-a1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    # 读取输入
    a = list(map(int, input().split()))

    # 排序
    a.sort()

    # 判断是否为等差数列
    if a[1] - a[0] == a[2] - a[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    l = input().split()
    l = list(map(int, l))
    l.sort()
    if l[2] - l[1] == l[1] - l[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    # 读取输入
    a1, a2, a3 = map(int, input().split())

    # 写入代码
    if a3 - a2 == a2 - a1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # 读入输入
    A = list(map(int, input().split()))
    # 排序
    A.sort()
    # 判断
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # 读取输入
    a = input()
    # 将输入的数字分割成字符串列表
    a_list = a.split()
    # 将字符串列表转化成数字列表
    a_list = [int(i) for i in a_list]
    # 将数字列表排序
    a_list.sort()
    # 将数字列表变成字符串
    a_list = [str(i) for i in a_list]
    # 将数字列表拼接成字符串
    a = "".join(a_list)
    # 判断是否为等差数列
    if a == "135":
        print("Yes")
    elif a == "555":
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    a = list(map(int, input().split()))
    a.sort()
    if (a[1] - a[0]) == (a[2] - a[1]):
        print('Yes')
    else:
        print('No')
