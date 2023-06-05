Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = input()
    b = a.split()
    b.sort()
    if (int(b[1]) - int(b[0])) == (int(b[2]) - int(b[1])):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a = input()
    a = a.split(" ")
    a = list(map(int,a))
    a.sort()
    if a[1] - a[0] == a[2] - a[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a = input()
    b = a.split(" ")
    c = []
    for i in b:
        c.append(int(i))
    c.sort()
    if c[2] - c[1] == c[1] - c[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[1] - A[0] == A[2] - A[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    # 读取输入
    A = list(map(int, input().split()))
    # 排序
    A.sort()
    # 判断是否是等差数列
    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    # Read three integers
    a1, a2, a3 = map(int, input().split())
    # Output Yes if a3-a2=a2-a1
    if a3-a2 == a2-a1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a = input()
    a = a.split()
    a = list(map(int, a))
    a.sort()
    if (a[2]-a[1])==(a[1]-a[0]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a = input().split()
    a.sort()
    if int(a[2]) - int(a[1]) == int(a[1]) - int(a[0]):
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 9

def main():
    a = [int(x) for x in input().split()]
    a.sort()
    if a[2]-a[1] == a[1]-a[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    a = input().split()
    a.sort()
    if int(a[1])-int(a[0]) == int(a[2])-int(a[1]):
        print("Yes")
    else:
        print("No")
