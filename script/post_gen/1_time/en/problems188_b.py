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
    ans = 0
    for i in range(n):
        ans += a[i]*b[i]
    if ans == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum = 0
    for i in range(0, n):
        sum += a[i] * b[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if sum([a[i] * b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = 0
    for i in range(N):
        C = C + A[i]*B[i]
    if C == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def inner_product():
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
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # print(N)
    # print(A)
    # print(B)

    # A = [1,3,5]
    # B = [3,-6,3]

    sum = 0
    for i in range(N):
        sum += A[i] * B[i]

    if sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def calculateInnerProduct(a,b):
    innerProduct = 0
    for i in range(len(a)):
        innerProduct += a[i]*b[i]
    return innerProduct
