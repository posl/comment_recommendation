Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a)-min(a))

=======
Suggestion 2

def max_difference(x):
    max = x[1]-x[0]
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if x[j]-x[i]>max:
                max = x[j]-x[i]
    return max

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1]-a[0])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_a = max(A)
    min_a = min(A)
    print(max_a - min_a)

=======
Suggestion 5

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    # compute
    max_abs = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(A[i]-A[j]) > max_abs:
                max_abs = abs(A[i]-A[j])
    # output
    print(max_abs)
    return

=======
Suggestion 6

def max_abs_diff():
    N = int(input())
    A = list(map(int, input().split()))
    max_A = max(A)
    min_A = min(A)
    print(max_A - min_A)

=======
Suggestion 7

def main():
    #输入
    n = int(input())
    a = list(map(int, input().split()))
    #处理
    a_max = max(a)
    a_min = min(a)
    max = a_max - a_min
    #输出
    print(max)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)
    print(max_a - min_a)
