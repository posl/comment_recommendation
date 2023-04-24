Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] < P:
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

=======
Suggestion 3

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] < P:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] < P:
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for a in A:
        if a < P:
            count += 1
    print(count)
