Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += a[i] * b[i]

    print("Yes" if sum == 0 else "No")

=======
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += a[i] * b[i]
    if ans == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

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
Suggestion 5

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
Suggestion 6

def solve():
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

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += A[i] * B[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

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
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    s = 0
    for i in range(n):
        s += a[i] * b[i]
    if s == 0:
        print("Yes")
    else:
        print("No")
