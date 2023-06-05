Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    result = []
    for i in range(n):
        if a[i] != x:
            result.append(a[i])
    print(*result)

=======
Suggestion 2

def problem191_b():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i],end=" ")
    print()

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        if i != x:
            print(i, end=" ")
    print()

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(*[i for i in a if i != x])

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=' ')

=======
Suggestion 6

def func():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=' ')

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    for i in l:
        if i != x:
            print(i, end=" ")

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=" ")

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    A = [i for i in A if i != X]

    print(*A)

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] != x:
            print(a[i], end=' ')
    print()
