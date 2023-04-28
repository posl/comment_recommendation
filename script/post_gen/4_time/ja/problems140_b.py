Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i] - 1]
        if i != n - 1 and a[i] + 1 == a[i + 1]:
            satisfaction += c[a[i] - 1]
    print(satisfaction)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i] - 1]
        if i > 0 and A[i] - A[i - 1] == 1:
            satisfaction += C[A[i - 1] - 1]

    print(satisfaction)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(i)-1 for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans += b[a[i]]
        if i != n-1 and a[i]+1 == a[i+1]:
            ans += c[a[i]]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int,input().split()))
    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i != n-1 and a[i+1] - a[i] == 1:
            satisfaction += c[a[i]-1]
    print(satisfaction)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int,input().split()))
    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i < n - 1 and a[i+1] - a[i] == 1:
            satisfaction += c[a[i]-1]
    print(satisfaction)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i < n-1 and a[i]+1 == a[i+1]:
            satisfaction += c[a[i]-1]

    print(satisfaction)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))


    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i < n-1 and a[i] == a[i+1]-1:
            satisfaction += c[a[i]-1]

    print(satisfaction)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += B[A[i] - 1]
        if i != N - 1 and A[i + 1] == A[i] + 1:
            sum += C[A[i] - 1]
    print(sum)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    happiness = 0
    for i in range(n):
        happiness += b[a[i]-1]
        if i < n-1 and a[i]+1 == a[i+1]:
            happiness += c[a[i]-1]
    print(happiness)

=======
Suggestion 10

def main():
    # coding: utf-8
    # Your code here!
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    total = 0
    for i in range(n):
        total += b[a[i]-1]
        if i > 0 and a[i]-1 == a[i-1]:
            total += c[a[i-1]-1]
    
    print(total)
