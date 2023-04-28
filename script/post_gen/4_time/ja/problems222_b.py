Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if a[i] < P:
            cnt += 1
    print(cnt)

main()

=======
Suggestion 3

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in a:
        if i < p:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if i < p:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        if a[i] < P:
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n,p = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] < p:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    cnt = 0
    for i in range(N):
        if A[i] < P:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    # input
    n, p = map(int, input().split())
    a = list(map(int, input().split()))

    # compute
    cnt = 0
    for i in range(n):
        if a[i] < p:
            cnt += 1

    # output
    print(cnt)

=======
Suggestion 9

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(n - a.count(p))

=======
Suggestion 10

def count_kadai():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)
