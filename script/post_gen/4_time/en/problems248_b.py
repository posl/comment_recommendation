Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    A, B, K = map(int, input().split())
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)

=======
Suggestion 2

def main():
    A, B, K = map(int, input().split())
    cnt = 0
    while A < B:
        cnt += 1
        A *= K
    print(cnt)

=======
Suggestion 3

def main():
    a, b, k = map(int, input().split())
    if a >= b:
        print(0)
    else:
        count = 0
        while a < b:
            a *= k
            count += 1
        print(count)

=======
Suggestion 4

def main():
    a,b,k = map(int, input().split())
    count = 0
    while a < b:
        a = a * k
        count = count + 1
    print(count)

=======
Suggestion 5

def solve(a, b, k):
    cnt = 0
    while a < b:
        a = a * k
        cnt = cnt + 1
    return cnt

=======
Suggestion 6

def solve():
    #import sys
    #input = sys.stdin.readline
    a,b,k = map(int, input().split())
    ans = 0
    while a < b:
        a *= k
        ans += 1
    print(ans)

=======
Suggestion 7

def problems248_b(a,b,k):
    count = 0
    while a < b:
        a *= k
        count += 1
    return count

=======
Suggestion 8

def main():
    A,B,K = map(int,input().split())
    cnt = 0
    while A < B:
        B = B - A
        cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    A,B,K = map(int,input().split())
    x = A
    for i in range(K):
        if x >= B:
            break
        x = x * K
    print(i)

=======
Suggestion 10

def solve(a, b, k):
    if b <= k:
        return 0
    if a >= k:
        return 1
    if a < k and b > k:
        return 2
    return 0
