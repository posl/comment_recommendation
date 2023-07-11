Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    flag = True
    for i in range(n-1):
        if a[i] == a[i+1]:
            f

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    set_A = set(A)
    if len(set_A) == N:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1,n):
        if a[i-1] == a[i]:

=======
Suggestion 6

def main():
    n = int(input())
    a = input().split()
    b = set(a)
    if len(b) == n:
        print('YES')
    else:
        print('NO')

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) == len(set(A)):
        print("YES")
    else:
        print("NO")
