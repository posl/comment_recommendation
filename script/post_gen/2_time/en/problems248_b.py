Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    count = 0
    while a < b:
        a *= k
        count += 1
    print(count)

=======
Suggestion 2

def main():
    A, B, K = map(int, input().split())
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)

=======
Suggestion 3

def solve():
    A, B, K = map(int, input().split())
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)

=======
Suggestion 4

def main():
    a, b, k = map(int, input().split())
    count = 0
    while True:
        if a >= b:
            break
        a *= k
        count += 1
    print(count)

=======
Suggestion 5

def problem248_b():
    a, b, k = map(int, input().split())
    cnt = 0
    while a < b:
        a = a * k
        cnt += 1
    print(cnt)

=======
Suggestion 6

def solve(A, B, K):
    count = 0
    while A < B:
        A = A * K
        count = count + 1
    return count

=======
Suggestion 7

def solve(a, b, k):
    if a >= b:
        return 0
    else:
        count = 0
        while a < b:
            a = a * k
            count += 1
        return count

=======
Suggestion 8

def main():
    a,b,k=map(int,input().split())
    count=0
    while a<b:
        a=a*k
        count=count+1
    print(count)

=======
Suggestion 9

def solve():
    a,b,k = map(int, input().split())
    if a >= b:
        print(0)
    else:
        print((b - a - 1) // (k - 1) + 1)
