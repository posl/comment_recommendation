Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    a, b, k = map(int, input().split())
    ans = 0
    while a < b:
        ans += 1
        a *= k
    print(ans)

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    count = 0
    while a < b:
        a = a * k
        count += 1
    print(count)

=======
Suggestion 3

def solve():
    a,b,k = map(int, input().split())
    if a >= b:
        print(0)
        return
    ans = 0
    while a < b:
        a += a * k
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    a, b, k = map(int, input().split())
    count = 0
    while a < b:
        a *= k
        count += 1
    print(count)

=======
Suggestion 5

def solve(a,b,k):
    #print(a,b,k)
    if a >= b:
        return 0
    if k == 1:
        return b-a
    count = 0
    while a < b:
        a = a*k
        count += 1
    return count

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

def solve(a, b, k):
    cnt = 0
    while a < b:
        a = a * k
        cnt += 1
    return cnt

=======
Suggestion 8

def problem248_b():
    a,b,k = map(int, input().split())
    c = 0
    while a < b:
        a = a * k
        c = c + 1
    print(c)
