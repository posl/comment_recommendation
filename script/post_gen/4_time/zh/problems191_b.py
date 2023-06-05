Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i], end=' ')

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))

    for i in range(n):
        if a[i] != x:
            print(a[i], end=' ')

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    nums = list(map(int,input().split()))
    for i in range(n):
        if nums[i] != x:
            print(nums[i],end=' ')

=======
Suggestion 4

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i],end=" ")
    print()

=======
Suggestion 5

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i],end=' ')
    print()

=======
Suggestion 6

def removeX(l, x):
    if len(l) == 0:
        return []
    elif len(l) == 1:
        if l[0] == x:
            return []
        else:
            return l
    else:
        if l[0] == x:
            return removeX(l[1:], x)
        else:
            return [l[0]] + removeX(l[1:], x)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        if i != x:
            print(i, end=' ')
    print()

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(*[i for i in a if i != x])

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i for i in a if i != x]
    print(*a)
