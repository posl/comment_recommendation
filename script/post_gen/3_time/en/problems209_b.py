Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        if i % 2 == 1:
            total += A[i] - 1
        else:
            total += A[i]

    if total <= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

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
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if (i + 1) % 2 == 0:
            sum += a[i] - 1
        else:
            sum += a[i]
    if sum <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if (i+1)%2 == 0:
            sum += a[i]-1
        else:
            sum += a[i]
    if sum <= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        if i%2 == 0:
            sum += A[i]
        else:
            sum += A[i] - 1
    if sum <= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def problems209_b():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if i % 2 == 1:
            s += a[i] - 1
        else:
            s += a[i]
    if s <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n,x = map(int, input().split())
    a_list = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += a_list[i]
        else:
            total += a_list[i] - 1
    if total <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def check(x,n,a):
    for i in range(n):
        if i%2==0:
            x-=a[i]
        else:
            x-=a[i]-1
        if x<0:
            return False
    return True

n,x=map(int,input().split())
a=list(map(int,input().split()))

=======
Suggestion 9

def main():
    # Get the input
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    # Process
    total = 0
    for i in range(n):
        if i % 2 == 1:
            total += a[i] - 1
        else:
            total += a[i]

    # Output
    if total <= x:
        print("Yes")
    else:
        print("No")
