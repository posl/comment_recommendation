Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    sum = 0
    for i in range(N):
        sum += A[i]*B[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    sum = 0
    for i in range(n):
        sum = sum + a[i] * b[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if sum([x*y for x, y in zip(a, b)]) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    for i in range(n):
        c += a[i] * b[i]
    if c == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    if sum == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if sum([a[i]*b[i] for i in range(n)]) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def dot_product(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = 0
    for i in range(n):
        result += a[i] * b[i]
    if result == 0:
        print("Yes")
    else:
        print("No")
