Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    for i in range(n):
        c += a[i]*b[i]
    if c == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print('Yes' if sum([a[i]*b[i] for i in range(n)]) == 0 else 'No')

=======
Suggestion 3

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
Suggestion 4

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
Suggestion 5

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
Suggestion 6

def is_zero_product(n, a, b):
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    if sum == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

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
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    for i in range(n):
        res += a[i]*b[i]
    if res == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([a[i] * b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")
