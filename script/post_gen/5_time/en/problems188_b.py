Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    for i in range(n):
        c += a[i] * b[i]
    if c == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    inner_product = 0
    for i in range(n):
        inner_product += a[i] * b[i]

    if inner_product == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

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
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    result = 0
    for i in range(n):
        result += a[i] * b[i]
    if result == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n):
        a[i] *= b[i]

    if sum(a) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    res = 0
    for i in range(N):
        res += A[i]*B[i]
    if res == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def inner_product(A, B):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
    return sum

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dot = 0
    for i in range(n):
        dot += a[i]*b[i]
    print('Yes' if dot == 0 else 'No')

solve()

=======
Suggestion 10

def inner_product():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([a[i] * b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")

inner_product()
