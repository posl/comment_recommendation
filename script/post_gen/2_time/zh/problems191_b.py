Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i],end=" ")

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i for i in a if i != x]
    print(*a)

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    for i in a:
        if i != x:
            print(i,end=' ')

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A_ = []
    for i in range(N):
        if A[i] != X:
            A_.append(A[i])
    for i in range(len(A_)):
        if i == len(A_)-1:
            print(A_[i])
        else:
            print(A_[i], end=" ")

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i], end=' ')
    print()

=======
Suggestion 6

def problems191_b():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i for i in a if i != x]
    print(*a)

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i],end=' ')
    print()

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[i] != x:
            ans.append(a[i])
    print(*ans)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i], end=' ')
