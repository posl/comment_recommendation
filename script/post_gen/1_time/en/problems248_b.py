Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    count = 0
    while A < B:
        A = A * K
        count += 1
    print(count)

=======
Suggestion 2

def problems248_b():
    a, b, k = map(int, input().split())
    cnt = 0
    while a < b:
        a *= k
        cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    a, b, k = map(int, input().split())
    n = 0
    while a < b:
        a *= k
        n += 1
    print(n)

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    count = 0
    while A <= B:
        count += 1
        A *= K
    print(count)

=======
Suggestion 5

def solve():
    A, B, K = map(int, input().split())
    ans = 0
    while B > A:
        A *= K
        ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    a,b,k = map(int,input().split())
    count = 0
    while a < b:
        a *= k
        count += 1
    print(count)

=======
Suggestion 7

def get_input():
    a, b, k = map(int, input().split())
    return (a, b, k)

=======
Suggestion 8

def get_input():
    return map(int, input().split())
