Synthesizing 10/10 solutions

=======
Suggestion 1

def problems134_c():
    pass

=======
Suggestion 2

def find_max_except_i(n, a):
    a.sort()
    for i in range(n):
        if i == 0:
            print(a[-1])
        elif i == n - 1:
            print(a[-2])
        else:
            if a[-1] == a[-2]:
                print(a[-1])
            else:
                if a[i] == a[-1]:
                    print(a[-2])
                else:
                    print(a[-1])

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))

    max_value = max(A)
    max_index = A.index(max_value)

    for i in range(N):
        if i == max_index:
            print(max(A[:max_index] + A[max_index + 1:]))
        else:
            print(max_value)

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    for i in range(n):
        if a[i] != max_a:
            print(max_a)
        else:
            print(sorted(a[:-1])[-1])

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    m = max(a)
    for i in a:
        if i == m:
            print(max(a[:a.index(m)] + a[a.index(m) + 1:]))
        else:
            print(m)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max1 = max(A)
    for i in range(N):
        if A[i] == max1:
            A.pop(i)
            break
    for i in range(N-1):
        print(max(A))

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max_count = a.count(a_max)
    if a_max_count == 1:
        for i in range(n):
            if a[i] == a_max:
                print(max(a[:i] + a[i+1:]))
            else:
                print(a_max)
    else:
        for i in range(n):
            print(a_max)

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))

    max_A = max(A)
    for i in range(N):
        if A[i] == max_A:
            print(max(A[:i] + A[i+1:]))
        else:
            print(max_A)

=======
Suggestion 9

def max_num(num_list):
    max_num = 0
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

=======
Suggestion 10

def main():
    n=int(input())
    a=[]
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        b=a[0:i]+a[i+1:n]
        print(max(b))
