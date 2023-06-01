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
    return

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            print('NO')
            return
    print('YES')
    return

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N - 1):
        if A[i] == A[i + 1]:
            print("NO")
            return
    print("YES")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n):
        if a[i-1] == a[i]:
            print('NO')
            break
    else:
        print('YES')

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print('NO')
            exit()
    print('YES')
main()

=======
Suggestion 8

def main():
    n = int(input())
    a = input().split()
    if len(set(a)) == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int,input().split()))
    print("Yes" if len(set(a)) == n else "No")
