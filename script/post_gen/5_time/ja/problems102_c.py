Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = a[n // 2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - i - 1
    B.sort()
    if N % 2 == 1:
        b = B[N//2]
    else:
        b = (B[N//2-1] + B[N//2]) // 2
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b + i + 1))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    b = A[N//2]
    total = 0
    for i in range(N):
        total += abs(A[i] - (b+i+1))
    print(total)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    if n%2 == 0:
        b = a[n//2-1]
    else:
        b = a[n//2]
    #print(b)
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b+i+1))
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = 0
    for i in range(n):
        b += a[i] - (i+1)
    print(b)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    b = A[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b+i+1))
    print(ans)

=======
Suggestion 7

def calc(a,b):
    return abs(a-b)

n = int(input())
a = list(map(int,input().split()))
a.sort()
b = a[n//2]
ans = 0
for i in range(n):
    ans += calc(a[i],b)
print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ans = 0
    for i in range(n):
        ans += abs(a[i] - a[n//2])

    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = 0
    for i in range(n):
        b += a[i] - (i+1)
    b = b // n
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b+i+1))
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    a = sorted(a)
    #print(a)
    b = a[n//2]
    #print(b)
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b)
    print(ans)
