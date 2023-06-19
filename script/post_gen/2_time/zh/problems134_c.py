Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max = max(A)
    for i in range(N):
        if A[i] == max:
            print(max(A[0:i]+A[i+1:N]))
        else:
            print(max)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    for i in range(N):
        print(max(A[:i]+A[i+1:]))

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_b = max(a[:a.index(max_a)] + a[a.index(max_a)+1:])
    for i in range(n):
        if a[i] == max_a:
            print(max_b)
        else:
            print(max_a)

=======
Suggestion 4

def max_num(num_list):
    max_num = max(num_list)
    return max_num

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max2 = sorted(a)[-2]
    for i in range(n):
        if a[i] == a_max:
            print(a_max2)
        else:
            print(a_max)

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max = 0
    for i in range(n):
        if max < a[i]:
            max = a[i]
    for i in range(n):
        if max == a[i]:
            a[i] = 0
    for i in range(n):
        print(max(a))

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    for i in range(N):
        a = int(input())
        A.append(a)
    for i in range(N):
        A.pop(i)
        print(max(A))
        A.insert(i, A.pop(i))

=======
Suggestion 8

def main():
    N=int(input())
    A=[]
    for i in range(N):
        A.append(int(input()))
    for i in range(N):
        A_copy=A.copy()
        A_copy.remove(A[i])
        print(max(A_copy))
main()

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        print(max(a[:i]+a[i+1:]))
main()
