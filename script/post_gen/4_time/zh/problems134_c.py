Synthesizing 10/10 solutions

=======
Suggestion 1

def problems134_c():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max_2nd = sorted(a)[-2]

    for i in range(n):
        if a[i] == a_max:
            print(a_max_2nd)
        else:
            print(a_max)

=======
Suggestion 2

def problems134_c():
    return None

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    max = A[N-1]
    for i in range(N):
        if A[i] < max:
            print(max)
        else:
            print(A[N-2])

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    for i in range(n):
        if a[i] == a_max:
            print(max(a[:i] + a[i+1:]))
        else:
            print(a_max)

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_a = max(a)
    for i in range(n):
        if a[i] == max_a:
            print(max(a[:i] + a[i+1:]))
        else:
            print(max_a)

=======
Suggestion 6

def main():
    n = int(input())
    A = []
    for i in range(n):
        A.append(int(input()))
    for i in range(n):
        print(max(A[:i]+A[i+1:]))

=======
Suggestion 7

def main():
    # N = int(input())
    # A = []
    # for i in range(N):
    #     A.append(int(input()))
    # for i in range(N):
    #     tmp = A[i]
    #     A[i] = 0
    #     print(max(A))
    #     A[i] = tmp
    # 以上是自己写的，但是会超时
    # 以下是参考答案
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max_num = max(A)
    max_num2 = max(A[:A.index(max_num)] + A[A.index(max_num) + 1:])
    for i in range(N):
        if A[i] == max_num:
            print(max_num2)
        else:
            print(max_num)

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    a.remove(a_max)
    for i in range(n):
        print(a_max)

main()

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    max_a = max(a)
    max_a_index = a.index(max_a)
    for i in range(n):
        if i == max_a_index:
            print(max(a[:max_a_index] + a[max_a_index+1:]))
        else:
            print(max_a)

=======
Suggestion 10

def problems134_c():
    pass
