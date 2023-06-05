Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 从标准输入读取
    a1, a2, a3, a4 = map(int, input().split())
    # 从小到大排序
    a = sorted((a1, a2, a3, a4))
    # 用第三大的数来除以400，得到可以举行的最大竞赛数量
    print(a[2] // 400)

=======
Suggestion 2

def problem185_a():
    A = input().split()
    for i in range(4):
        A[i] = int(A[i])
    A.sort()
    if A[0] + A[1] + A[2] >= A[3]:
        print(3)
    else:
        print(4)

=======
Suggestion 3

def solve():
    A = list(map(int, input().split()))
    A.sort()
    if A[0] + A[1] + A[2] >= A[3]:
        print(1)
    else:
        print(0)

=======
Suggestion 4

def main():
    a = input()
    a = a.split()
    a = [int(i) for i in a]
    print(min(a))

=======
Suggestion 5

def solve():
	a = list(map(int, input().split()))
	a.sort()
	print(a[0])

=======
Suggestion 6

def solve():
    A = list(map(int, input().split()))
    A.sort()
    if A[0] + A[1] + A[2] + A[3] <= 300:
        print(1)
    elif A[0] + A[1] + A[2] <= 300 or A[1] + A[2] + A[3] <= 300:
        print(2)
    else:
        print(3)

=======
Suggestion 7

def problem185_a():
    a = [int(i) for i in input().split()]
    a.sort()
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[0]+a[1]+a[2])
    print(a[0]+a[1]+a[3])
    print(a[0]+a[2]+a[3])
    print(a[1]+a[2]+a[3])
    print(a[0]+a[1]+a[2]+a[3])
    return

=======
Suggestion 8

def main():
    a1,a2,a3,a4 = map(int,input().split())
    print(min(a1,a2,a3,a4))

=======
Suggestion 9

def main():
    # 读入数据
    A = list(map(int, input().split()))
    # print(A)
    # 处理数据
    A.sort()
    # print(A)
    # 输出数据
    print(A[0])

=======
Suggestion 10

def solve():
    A = list(map(int, input().split()))
    print(min(A[0], A[1], A[2], A[3]))
