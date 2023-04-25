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
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] < P:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        if a < P:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for a in A:
        if a < P:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(len(A)):
        if A[i] < P:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    print(sum([1 for a in A if a < P]))

=======
Suggestion 7

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(1 for i in a if i < p))
