Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if len(set(a)) == len(a) else "NO")

=======
Suggestion 2

def checkpair():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")

=======
Suggestion 3

def check_unique(a):
    if len(a) == len(set(a)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    flag = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            flag = 1
            break
    if flag == 1:
        print('NO')
    else:
        print('YES')

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n):
        if a[i - 1] == a[i]:
            print('NO')
            return
    print('YES')

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if(a[i] == a[i+1]):
            print("NO")
            return
    print("YES")
    return

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print('YES')
    else:
        print('NO')

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n):
        if a[i - 1] == a[i]:
            print('NO')
            break
    else:
        print('YES')

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")
main()
