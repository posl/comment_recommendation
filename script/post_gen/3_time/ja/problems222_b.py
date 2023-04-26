Synthesizing 10/10 solutions (Duplicates hidden)

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
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] < P:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] < P:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if A[i] < P:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N,P = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    for i in a:
        if i < P:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([i for i in a if i < P]))

=======
Suggestion 7

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([x for x in a if x < P]))

=======
Suggestion 8

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    print(sum([1 for a in A if a < P]))

=======
Suggestion 9

def main():
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    print(len([a for a in A if a < P]))
