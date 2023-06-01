Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a)-min(a))

=======
Suggestion 2

def max_difference(a):
    max = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                if abs(a[i] - a[j]) > max:
                    max = abs(a[i] - a[j])
    return max

a = []
n = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
print(max_difference(a))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1] - a[0])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_num = max(A)
    min_num = min(A)
    print(max_num - min_num)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-1]-A[0])

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(max(a)-min(a))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(abs(max(A)-min(A)))

=======
Suggestion 8

def main():
    n = int(input())
    a = input().split()
    a = list(map(int,a))
    max = 0
    for i in range(n):
        for j in range(i+1,n):
            if abs(a[i] - a[j]) > max:
                max = abs(a[i] - a[j])
    print(max)

=======
Suggestion 9

def max_diff():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(A[i] - A[j]) > max:
                max = abs(A[i] - A[j])
    print(max)

max_diff()
