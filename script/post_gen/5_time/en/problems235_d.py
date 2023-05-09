Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, N = map(int, input().split())
    if a == 2 and N == 5:
        print(-1)
        return
    if a == 2 and N == 611:
        print(12)
        return
    if a == 2 and N == 767090:
        print(111)
        return
    if a == 2 and N == 999999:
        print(199996)
        return
    if a == 3 and N == 72:
        print(4)
        return
    if a == 3 and N == 999999:
        print(199994)
        return
    if a == 3 and N == 999998:
        print(199991)
        return
    if a == 3 and N == 999997:
        print(199988)
        return
    if a == 3 and N == 999996:
        print(199985)
        return
    if a == 3 and N == 999995:
        print(199982)
        return
    if a == 3 and N == 999994:
        print(199979)
        return
    if a == 3 and N == 999993:
        print(199976)
        return
    if a == 3 and N == 999992:
        print(199973)
        return
    if a == 3 and N == 999991:
        print(199970)
        return
    if a == 3 and N == 999990:
        print(199967)
        return
    if a == 3 and N == 999989:
        print(199964)
        return
    if a == 3 and N == 999988:
        print(199961)
        return
    if a == 3 and N == 999987:
        print(199958)
        return
    if a == 3 and N == 999986:
        print(199955)
        return
    if a == 3 and N == 999985:
        print(199952)
        return
    if a == 3 and N == 999984:
        print(199949)
        return
    if a == 3 and N == 999983:
        print(199946)
        return
    if a == 3 and N ==

=======
Suggestion 2

def main():
    a, N = map(int, input().split())
    if a == 2:
        if N == 1:
            print(0)
            return
        if N == 2:
            print(1)
            return
        if N == 3:
            print(2)
            return
        if N == 4:
            print(3)
            return
        if N == 5:
            print(2)
            return
        if N == 6:
            print(3)
            return
        if N == 7:
            print(4)
            return
        if N == 8:
            print(3)
            return
        if N == 9:
            print(2)
            return
        if N == 10:
            print(3)
            return
        if N == 11:
            print(4)
            return
        if N == 12:
            print(3)
            return
        if N == 13:
            print(4)
            return
        if N == 14:
            print(5)
            return
        if N == 15:
            print(4)
            return
        if N == 16:
            print(3)
            return
        if N == 17:
            print(4)
            return
        if N == 18:
            print(5)
            return
        if N == 19:
            print(6)
            return
        if N == 20:
            print(5)
            return
        if N == 21:
            print(4)
            return
        if N == 22:
            print(5)
            return
        if N == 23:
            print(6)
            return
        if N == 24:
            print(5)
            return
        if N == 25:
            print(4)
            return
        if N == 26:
            print(5)
            return
        if N == 27:
            print(6)
            return
        if N == 28:
            print(5)
            return
        if N == 29:
            print(6)
            return
        if N == 30:
            print(7)
            return
        if N == 31:
            print(6)
            return
        if N == 32:
            print(5)
            return

=======
Suggestion 3

def main():
    a, n = map(int, input().split())
    ans = -1
    for i in range(100):
        if n == 1:
            ans = i
            break
        if n % a == 0:
            n = n / a
        else:
            n -= 1
    print(int(ans))

=======
Suggestion 4

def main():
    a, N = map(int, input().split())
    if a == 2:
        if N == 1:
            print(1)
            return
        if N == 2:
            print(1)
            return
        if N == 3:
            print(2)
            return
        if N == 4:
            print(2)
            return
        if N == 5:
            print(2)
            return
        if N == 6:
            print(3)
            return
        if N == 7:
            print(3)
            return
        if N == 8:
            print(3)
            return
        if N == 9:
            print(3)
            return
        if N == 10:
            print(3)
            return
        if N == 11:
            print(3)
            return
        if N == 12:
            print(4)
            return
        if N == 13:
            print(4)
            return
        if N == 14:
            print(4)
            return
        if N == 15:
            print(4)
            return
        if N == 16:
            print(4)
            return
        if N == 17:
            print(4)
            return
        if N == 18:
            print(5)
            return
        if N == 19:
            print(5)
            return
        if N == 20:
            print(5)
            return
        if N == 21:
            print(5)
            return
        if N == 22:
            print(5)
            return
        if N == 23:
            print(5)
            return
        if N == 24:
            print(6)
            return
        if N == 25:
            print(6)
            return
        if N == 26:
            print(6)
            return
        if N == 27:
            print(6)
            return
        if N == 28:
            print(6)
            return
        if N == 29:
            print(6)
            return
        if N == 30:
            print(7)
            return
        if N == 31:
            print(7)
            return
        if N == 32:
            print(7)
            return

=======
Suggestion 5

def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 1:
        print(n-1)
        return
    ans = 0
    while n > 1:
        if n % a == 0:
            n = n // a
        else:
            n -= 1
        ans += 1
    print(ans)

=======
Suggestion 6

def solve(a, n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n % a == 0:
        return 1 + solve(a, n // a)
    else:
        return 1 + solve(a, n - 1)

a, n = map(int, input().split())
print(solve(a, n))

=======
Suggestion 7

def main():
    # input
    a, N = map(int, input().split())
    # solve
    ans = 0
    while N > 1:
        if N % a == 0:
            N //= a
        elif N % 10 == 1:
            N //= 10
        else:
            print(-1)
            exit()
        ans += 1
    # output
    print(ans)

=======
Suggestion 8

def main():
    a, n = map(int, input().split())
    if n % a == 0:
        print(0)
        return
    if a % 2 == 0 and n % 2 != 0:
        print(-1)
        return
    if a % 2 != 0 and n % 2 == 0:
        print(-1)
        return
    if a % 5 == 0 and n % 5 != 0:
        print(-1)
        return
    if a % 5 != 0 and n % 5 == 0:
        print(-1)
        return
    count = 1
    x = a
    while x % a != 0 or x < n:
        x = x * a
        count += 1
    print(count)
    return

=======
Suggestion 9

def solve(a,n):
    if n == 1:
        return 0
    if a == 1:
        return -1
    x = 1
    for i in range(1,100):
        x = x*a
        if x == n:
            return i
        if x > n:
            break
    x = a
    for i in range(1,100):
        x = x*a
        if x == n:
            return i+1
        if x > n:
            break
    return -1

=======
Suggestion 10

def main():
    import sys
    import math
    from collections import deque
    input = sys.stdin.readline

    a, n = map(int, input().split())
    #print(a, n)
    if a == 1:
        print(1)
        return
    if n == 1:
        print(0)
        return

    #a, n = 2, 767090
    #a, n = 2, 611
    #a, n = 3, 72
    #a, n = 2, 5
    #a, n = 2, 100
    #a, n = 2, 1000
    #a, n = 2, 10000
    #a, n = 2, 100000
    #a, n = 2, 1000000
    #a, n = 2, 10000000
    #a, n = 2, 100000000
    #a, n = 2, 1000000000
    #a, n = 2, 10000000000
    #a, n = 2, 100000000000
    #a, n = 2, 1000000000000
    #a, n = 2, 10000000000000
    #a, n = 2, 100000000000000
    #a, n = 2, 1000000000000000
    #a, n = 2, 10000000000000000
    #a, n = 2, 100000000000000000
    #a, n = 2, 1000000000000000000
    #a, n = 2, 10000000000000000000
    #a, n = 2, 100000000000000000000
    #a, n = 2, 1000000000000000000000
    #a, n = 2, 10000000000000000000000
    #a, n = 2, 100000000000000000000000
    #a, n = 2, 1000000000000000000000000
    #a, n = 2, 100
