Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i], end=' ')

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(*[i for i in a if i != x])

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(' '.join([str(i) for i in a if i != x]))

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A_ = [a for a in A if a != X]
    print(*A_)

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] == x:
            a[i] = 0
    for i in range(n):
        if a[i] != 0:
            print(a[i],end=" ")

=======
Suggestion 6

def get_input():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    return n, x, a

=======
Suggestion 7

def solve():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    ans = []
    for i in A:
        if i != X:
            ans.append(i)
    print(*ans)

=======
Suggestion 8

def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    print(" ".join([str(i) for i in a if i != x]))

=======
Suggestion 9

def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    print(' '.join(list(map(str, filter(lambda x: x != n, a)))))
