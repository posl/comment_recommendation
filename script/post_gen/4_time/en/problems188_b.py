Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    inner_product = 0
    for i in range(N):
        inner_product += A[i] * B[i]
    if inner_product == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += a[i] * b[i]
    print('Yes' if s == 0 else 'No')

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    s = 0
    for i in range(n):
        s += a[i] * b[i]
    if s == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([a[i]*b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = 0
    for i in range(n):
        c += a[i] * b[i]
    if c == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        ans += a[i] * b[i]
    
    if ans == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def inner_product(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([x*y for x,y in zip(a, b)]) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def calc_inner_product(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

=======
Suggestion 10

def inner_product(a, b):
    result = 0
    for i in range(0, len(a)):
        result += a[i] * b[i]
    return result

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

print("Yes" if inner_product(a, b) == 0 else "No")
