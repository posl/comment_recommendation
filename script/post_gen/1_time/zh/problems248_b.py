Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    ans = 0
    while a < b:
        a += (a * k)
        ans += 1
    print(ans)

=======
Suggestion 2

def solve(a, b, k):
    ans = 0
    while a < b:
        a = a * k
        ans += 1
    return ans

=======
Suggestion 3

def solve(a,b,k):
    cnt = 0
    while a < b:
        a = a * k
        cnt += 1
    return cnt

=======
Suggestion 4

def main():
    import sys
    input = sys.stdin.readline
    a, b, k = map(int, input().split())
    ans = 0
    while a < b:
        a *= k
        ans += 1
    print(ans)

=======
Suggestion 5

def problem248_b(a,b,k):
    count=0
    while a<b:
        a*=k
        count+=1
    return count

=======
Suggestion 6

def main():
    a,b,k = map(int,input().split())
    count = 0
    while a<b:
        a += a*(k-1)
        count += 1
    print(count)

=======
Suggestion 7

def main():
    A,B,K = map(int, input().split())
    ans = 0
    while A < B:
        A = A*K
        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    a, b, k = map(int, input().split())
    count = 0
    while a < b:
        a *= k
        count += 1
    print(count)

=======
Suggestion 9

def main():
    a,b,k = map(int,input().split())
    cnt = 0
    while a < b:
        a *= k
        cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    a,b,k = map(int, input().split())
    cnt = 0
    while a < b:
        a += a * (k - 1)
        cnt += 1
    print(cnt)
