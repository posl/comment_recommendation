Synthesizing 10/10 solutions

=======
Suggestion 1

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))

=======
Suggestion 2

def max_diff():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A) - min(A))

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(max(A)-min(A))

=======
Suggestion 4

def main():
    #读取输入
    n = int(input())
    a = list(map(int, input().split()))
    #初始化最大绝对差
    max_diff = 0
    #遍历所有可能的组合
    for i in range(n):
        for j in range(n):
            #如果是两个不同的元素
            if i != j:
                #计算绝对差
                diff = abs(a[i] - a[j])
                #如果绝对差大于最大绝对差
                if diff > max_diff:
                    #更新最大绝对差
                    max_diff = diff
    #打印最大绝对差
    print(max_diff)

=======
Suggestion 5

def max_diff(a):
    a.sort()
    return a[-1] - a[0]

=======
Suggestion 6

def abs_max(x):
    x.sort()
    return x[-1]-x[0]

n = int(input())
a = list(map(int,input().split()))
print(abs_max(a))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    max_num = max(A)
    min_num = min(A)

    print(max_num - min_num)

=======
Suggestion 8

def max_abs_diff(a):
    a.sort()
    return a[-1] - a[0]

=======
Suggestion 9

def problems102_b():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a)-min(a))

problems102_b()

=======
Suggestion 10

def max_diff(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if abs(arr[i]-arr[j])>max:
                max = abs(arr[i]-arr[j])
    return max
