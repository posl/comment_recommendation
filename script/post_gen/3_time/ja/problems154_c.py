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
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")
    return

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print('NO')
            return
    print('YES')
    return

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    if len(set(A)) == N:
        print("YES")
    else:
        print("NO")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    if len(set(A)) == N:
        print('YES')
    else:
        print('NO')

=======
Suggestion 7

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(n-1):
        if A[i] == A[i+1]:
            print('NO')
            return
    print('YES')
    return

=======
Suggestion 8

def main():
    N = int(input())
    A = input().split()
    if len(set(A)) == N:
        print("YES")
    else:
        print("NO")

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #ソート
    A.sort()
    #出力
    for i in range(N-1):
        if A[i] == A[i+1]:
            print('NO')
            return
    print('YES')
