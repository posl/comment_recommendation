Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # get input
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # calculate
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    # output
    if sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("length of a and b must be equal")
    product = 0
    for i in range(len(a)):
        product += a[i] * b[i]
    return product

=======
Suggestion 3

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
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    for i in range(n):
        c += a[i]*b[i]
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
    
    if sum([a[i]*b[i] for i in range(n)]) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = 0
    for i in range(n):
        result += a[i] * b[i]

    if result == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    if sum([a[i]*b[i] for i in range(n)]) == 0:
        print('Yes')
    else:
        print('No')
