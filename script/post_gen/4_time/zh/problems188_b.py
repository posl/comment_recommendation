Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("Yes" if sum([a[i]*b[i] for i in range(n)]) == 0 else "No")

=======
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dot = 0
    for i in range(n):
        dot += a[i] * b[i]

    if dot == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    inner_product = 0
    for i in range(n):
        inner_product += a[i] * b[i]
    if inner_product == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if sum([a[i] * b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print("Yes" if sum([A[i]*B[i] for i in range(N)]) == 0 else "No")

=======
Suggestion 7

def dot_product(A, B):
    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]
    return result

=======
Suggestion 8

def dot_product(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    for i in range(N):
        result += A[i] * B[i]
    if result == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")
