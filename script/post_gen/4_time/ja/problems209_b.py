Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if i % 2 == 1:
            sum += a[i] - 1
        else:
            sum += a[i]
    if sum <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += a[i]
        else:
            sum += a[i] - 1
    if sum <= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        if i % 2 == 1:
            sum += A[i] - 1
        else:
            sum += A[i]
    if sum <= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        if i % 2 == 1:
            sum += A[i] - 1
        else:
            sum += A[i]

    if sum <= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def solve():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        if i % 2 == 1:
            sum += A[i] - 1
        else:
            sum += A[i]
    if sum <= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        if i % 2 == 1:
            sum += a[i] - 1
        else:
            sum += a[i]
    if sum <= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(N):
        if i%2 == 0:
            sum += A[i]
        else:
            sum += A[i] - 1
    if X >= sum:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    total = 0
    for i in range(N):
        if i%2==1:
            total += A[i]-1
        else:
            total += A[i]
    if total <= X:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    A = map(int, input().split())

    if X >= sum(A) - N//2:
        print('Yes')
    else:
        print('No')
