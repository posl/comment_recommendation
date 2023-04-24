Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(set(A)) == N:
        print("YES")
    else:
        print("NO")

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) == len(set(A)):
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")

main()

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
    if len(set(a)) == n:
        print('YES')
    else:
        print('NO')

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")
    return

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if len(a) == len(set(a)) else "NO")
