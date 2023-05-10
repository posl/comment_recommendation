Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def func(a, b, k):
    cnt = 0
    while a < b:
        a *= k
        cnt += 1
    return cnt

a, b, k = map(int, input().strip().split())
print(func(a, b, k))

=======
Suggestion 2

def count_scream(a, b, k):
    count = 0
    while a < b:
        a *= k
        count += 1
    return count

a, b, k = map(int, input().split())
print(count_scream(a, b, k))

=======
Suggestion 3

def solve(A, B, K):
    cnt = 0
    while A < B:
        A *= K
        cnt += 1
    return cnt

=======
Suggestion 4

def main():
    # A,B,K = map(int, input().split())
    A,B,K = 31,415926,5
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)

=======
Suggestion 5

def solve():
    a,b,k = map(int,input().split())
    count = 0
    while a < b:
        a *= k
        count += 1
    print(count)

=======
Suggestion 6

def main():
    a,b,k = map(int,input().split())
    count = 0
    while a <= b:
        a *= k
        count += 1
    print(count)

=======
Suggestion 7

def main():
    a,b,k = map(int, input().split())
    cnt = 0
    while a < b:
        a *= k
        cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    A, B, K = map(int, input().split())
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)
