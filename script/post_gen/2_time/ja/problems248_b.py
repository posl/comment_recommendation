Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    ans = 0
    while a < b:
        a *= k
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    ans = 0
    while A < B:
        A *= K
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    cnt = 0
    while A < B:
        A *= K
        cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    a, b, k = map(int, input().split())
    cnt = 0
    while a < b:
        a *= k
        cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
        return
    if A * K >= B:
        print(B - A)
        return
    print(K)

=======
Suggestion 7

def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
    else:
        print(min(B - A, K))

=======
Suggestion 8

def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
    else:
        print(min(K, B - A))

=======
Suggestion 9

def main():
    A,B,K = map(int,input().split())
    if A >= B:
        print(0)
        return
    if K > A:
        print(A)
        return
    print(A-K)
