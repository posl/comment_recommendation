Synthesizing 10/10 solutions

=======
Suggestion 1

def isPopular(items, m):
    total = sum(items)
    for item in items:
        if item < total/(4*m):
            return False
    return True

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum >= sum(a) / (4 * m):
        print("是")
    else:
        print("否")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[m-1] >= total/(4*m):
        print('是')
    else:
        print('否')
main()

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    s = sum(a)
    for i in range(m):
        if a[i] < s/(4*m):
            print("否")
            return
    print("是")

=======
Suggestion 5

def problem161_b():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] * 4 * m < total:
            print('否')
            return
    print('是')

=======
Suggestion 6

def get_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    return n, m, a

=======
Suggestion 7

def is_popular(A, M):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    for i in range(len(A)):
        if A[i] < sum / (4 * M):
            return False
    return True

N, M = input().split()
N = int(N)
M = int(M)
A = list(map(int, input().split()))
A.sort(reverse=True)

=======
Suggestion 8

def problems161_b():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    sumA = sum(A)
    for i in range(m):
        if A[i] < sumA/(4*m):
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def problem161_b():
    n = 0
    m = 0
    a = []
    while True:
        try:
            line = input()
            if line:
                if n == 0:
                    n = int(line.split(' ')[0])
                    m = int(line.split(' ')[1])
                else:
                    a = line.split(' ')
            else:
                break
        except:
            break

    a = [int(i) for i in a]
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total/(4*m):
        print('是')
    else:
        print('否')

=======
Suggestion 10

def main():
    # 读入数据
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    # 排序
    A.sort(reverse=True)
    # 计算总票数
    s = sum(A)
    # 计算最小票数
    if s >= 4 * m * A[m - 1]:
        print("是")
    else:
        print("否")
