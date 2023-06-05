Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if a[i] < p:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def count_failed_student(N, P, scores):
    count = 0
    for i in range(N):
        if scores[i] < P:
            count = count + 1
    return count

=======
Suggestion 3

def main():
    N,P = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if a[i] < P:
            count += 1
    print(count)

=======
Suggestion 4

def get_input():
    N,P = map(int,input().split())
    a = list(map(int,input().split()))
    return N,P,a

=======
Suggestion 5

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] < P:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if i < P:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    cnt = 0
    for i in a:
        if i < p:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([1 for i in a if i < p]))

=======
Suggestion 9

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = [i for i in a if i < p]
    print(len(b))
