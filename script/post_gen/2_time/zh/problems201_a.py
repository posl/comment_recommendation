Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def isArithmeticSequence(A):
    A.sort()
    if A[2]-A[1]==A[1]-A[0]:
        return True
    else:
        return False

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    A = input()
    A = A.split()
    A = list(map(int, A))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def f():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")

f()

=======
Suggestion 5

def is_arithmetic_sequence(a1, a2, a3):
    if a3 - a2 == a2 - a1:
        return True
    else:
        return False

=======
Suggestion 6

def is_arithmetic_sequence(a1, a2, a3):
    if a1 == a2 == a3:
        return True
    elif a1 == a2 or a2 == a3:
        return False
    else:
        return (a3 - a2) == (a2 - a1)

=======
Suggestion 7

def problems201_a():
    A = input("请输入三个数字，以空格分隔：")
    A = A.split(' ')
    A = [int(i) for i in A]
    A.sort()
    if (A[2] - A[1]) == (A[1] - A[0]):
        print("Yes")
    else:
        print("No")
    return None

=======
Suggestion 8

def main():
    # 读取输入
    A = input().split()
    # 是否可以重新排列A的元素成为算术序列
    if int(A[2]) - int(A[1]) == int(A[1]) - int(A[0]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")
