Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] < P:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    cnt = 0
    for i in a:
        if i < p:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([x for x in a if x < p]))

=======
Suggestion 4

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([i for i in a if i < p]))

=======
Suggestion 5

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    print(len([a for a in A if a < P]))

=======
Suggestion 6

def problem222_b():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([i for i in a if i < p]))
