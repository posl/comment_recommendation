Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(set(A)) == N:
        print('YES')
    else:
        print('NO')

main()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(set(A)) == N:
        print('YES')
    else:
        print('NO')

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) != len(set(A)):
        print("NO")
    else:
        print("YES")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) != len(set(a)):
        print("NO")
    else:
        print("YES")

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) != len(set(A)):
        print('NO')
    else:
        print('YES')

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(1, N):
        if A[i-1] == A[i]:
            print("NO")
            return
    print("YES")

main()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print('NO')
            return
    print('YES')

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == len(set(a)):
        print("YES")
    else:
        print("NO")

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    if len(s) == n:
        print("YES")
    else:
        print("NO")

main()

This code got accepted.

I solved this problem on 2018/10/09.

I solved this problem on 2018/10/09.

Today I solved the following problem.
