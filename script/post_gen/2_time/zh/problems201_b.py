Synthesizing 10/10 solutions

=======
Suggestion 1

def problem201_a():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a,b,c=map(int,input().split())
    if b-a==c-b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[1] - A[0] == A[2] - A[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2]-a[1] == a[1]-a[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    #读取输入
    line = input()
    #将输入的字符串分割成3个数字
    A = line.split()
    #将字符串转换成数字
    #map(function, iterable, ...)
    #map() 会根据提供的函数对指定序列做映射。
    #第一个参数 function 以参数序列中的每一个元素调用 function 函数，
    #返回包含每次 function 函数返回值的新列表。
    #map() 函数语法：
    #map(function, iterable, ...)
    #参数
    #function -- 函数
    #iterable -- 一个或多个序列
    #返回值
    #Python 2.x 返回列表。
    #Python 3.x 返回迭代器。
    A = list(map(int, A))
    #判断A的元素能否重新排列成算术序列
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2]-A[1] == A[1]-A[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    a = input()
    a = a.split()
    a = [int(i) for i in a]
    a.sort()
    if (a[1]-a[0])==(a[2]-a[1]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    a = input().split()
    a = [int(i) for i in a]
    a.sort()
    if a[1] - a[0] == a[2] - a[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    a1,a2,a3 = map(int,input().split())
    if a3-a2 == a2-a1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    A = input().split()
    A.sort()
    if int(A[2])-int(A[1])==int(A[1])-int(A[0]):
        print("Yes")
    else:
        print("No")
