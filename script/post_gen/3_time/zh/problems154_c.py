Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    for i in range(0,n):
        if i == n-1:
            print("Yes")
            break
        if a[i] == a[i+1]:
            print("No")
            break

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    for i in range(N-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print('NO')
            exit()
    print('YES')

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) == len(set(a)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print("YES")
    else:
        print("NO")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            exit()
    print("YES")

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(0, N-1):
        if A[i] == A[i+1]:
            print("NO")
            exit()
    print("YES")

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    if len(a) == len(b):
        print('YES')
    else:
        print('NO')
