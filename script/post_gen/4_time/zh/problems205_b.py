Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n + 1):
        if a[i - 1] != i:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a == list(range(1,n+1)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def f():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == list(range(1, n+1)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def is_permutation(n, a):
    if len(a) != n:
        return False
    for i in range(1, n+1):
        if i not in a:
            return False
    return True

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i + 1:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A == list(range(1, N+1)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n+1):
        if a[i-1] != i:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n+1):
        if i != a[i-1]:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n+1):
        if a[i-1] != i:
            print('No')
            break
    else:
        print('Yes')
