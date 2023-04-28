Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=" ")

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[i] != x:
            ans.append(a[i])
    print(*ans)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    for i in a:
        if i != x:
            ans.append(i)
    print(*ans)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i for i in a if i != x]
    print(*a)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(*[i for i in a if i != x])

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(' '.join([str(i) for i in a if i != x]))

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(N):
        if A[i] != X:
            print(A[i], end=' ')

main()

=======
Suggestion 8

def problems191_b():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i for i in a if i != x]
    print(*a)

=======
Suggestion 9

def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    result = [i for i in a if i != x]
    for i in result:
        print(i, end=" ")
