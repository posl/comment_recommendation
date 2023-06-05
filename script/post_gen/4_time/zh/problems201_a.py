Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def isAP(a,b,c):
    if a-b == b-c:
        return True
    else:
        return False

a,b,c = map(int,input().split())

=======
Suggestion 2

def arithmetic_sequence(a1, a2, a3):
    if a3 - a2 == a2 - a1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if (c-b) == (b-a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def arithmetic_sequence():
    A = list(map(int,input().split()))
    A.sort()
    if A[2]-A[1]==A[1]-A[0]:
        print('Yes')
    else:
        print('No')

arithmetic_sequence()

=======
Suggestion 5

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def arithmetic_sequence(a1,a2,a3):
    if a3-a2 == a2-a1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    # 获取输入
    line = input()
    # 用空格分隔输入的三个数字
    A = line.split(" ")
    # 将字符串转换为整数
    A = [int(s) for s in A]
    # 排序
    A.sort()
    # 如果A_3-A_2=A_2-A_1，则打印“Yes”，否则打印“No”
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a = list(map(int,input().split()))
    a.sort()
    if a[1] - a[0] == a[2] - a[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def problems201_a():
    a = input()
    a = a.split(" ")
    a = [int(i) for i in a]
    a.sort()
    if a[2]-a[1] == a[1]-a[0]:
        print("Yes")
    else:
        print("No")
