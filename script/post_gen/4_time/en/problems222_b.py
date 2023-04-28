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
    n,p = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] < p:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def problems222_b():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] < P:
            ans += 1
    return ans

print(problems222_b())

=======
Suggestion 5

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = 0
    for i in range(n):
        if a[i] < p:
            b += 1
    print(b)

=======
Suggestion 6

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([x for x in a if x < p]))

=======
Suggestion 7

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    print(len([i for i in A if i < P]))

=======
Suggestion 8

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(1 for x in a if x < p))

=======
Suggestion 9

def failed_students():
    n, p = map(int, input().split())
    score = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if score[i] < p:
            count += 1
    print(count)

failed_students()
