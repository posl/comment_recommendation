Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, X = map(int, input().split())
    ans = 0
    if A * 10 ** 9 + B * 10 <= X:
        ans = 10 ** 9
    else:
        for i in range(1, 10):
            if A * i ** 9 + B * len(str(i)) <= X:
                ans = i
    print(ans)

=======
Suggestion 2

def main():
    a, b, x = map(int, input().split())
    #print(a, b, x)
    if a * 10 ** 9 + b * 10 <= x:
        print(10 ** 9)
        return
    if a + b >= x:
        print(0)
        return
    if a * 10 ** 9 + b * 1 >= x:
        print(1)
        return
    if a * 10 ** 9 + b * 2 >= x:
        print(2)
        return
    if a * 10 ** 9 + b * 3 >= x:
        print(3)
        return
    if a * 10 ** 9 + b * 4 >= x:
        print(4)
        return
    if a * 10 ** 9 + b * 5 >= x:
        print(5)
        return
    if a * 10 ** 9 + b * 6 >= x:
        print(6)
        return
    if a * 10 ** 9 + b * 7 >= x:
        print(7)
        return
    if a * 10 ** 9 + b * 8 >= x:
        print(8)
        return
    if a * 10 ** 9 + b * 9 >= x:
        print(9)
        return
    if a * 10 ** 9 + b * 10 >= x:
        print(10)
        return

=======
Suggestion 3

def main():
    a, b, x = map(int, input().split())
    if a * 10 + b * 1 <= x:
        print(10**9)
        return
    if a * 1 + b * 1 > x:
        print(0)
        return
    if a * 1 + b * 10 > x:
        print(x // b)
        return
    if a * 1 + b * 10 <= x:
        print((x - a * 1) // b)
        return

=======
Suggestion 4

def main():
    A, B, X = map(int, input().split())
    if A * 10**9 + B * 10 < X:
        print(10**9)
    else:
        ans = 0
        for i in range(1, 10):
            num = (X - B * i) // A
            if num < 10**i:
                ans = max(ans, num)
        print(ans)

=======
Suggestion 5

def main():
    a, b, x = map(int, input().split())
    print(max([n for n in range(1, 10**9) if a * n + b * len(str(n)) <= x]))

=======
Suggestion 6

def d(n):
    return len(str(n))

a,b,x = map(int, input().split())
ans = 0
for i in range(1,11):
    if a*i + b*d(i) <= x:
        ans = i
    else:
        break
print(ans)

=======
Suggestion 7

def solve():
    A, B, X = map(int, input().split())
    def price(n):
        return A * n + B * len(str(n))
    def bisect(ok, ng, p):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if p(mid) <= X:
                ok = mid
            else:
                ng = mid
        return ok
    print(bisect(0, 10 ** 9 + 1, price))

solve()

=======
Suggestion 8

def solve():
    A, B, X = map(int, input().split())
    #print(A, B, X)

    def cost(n):
        return A * n + B * len(str(n))

    def can_buy(n):
        return cost(n) <= X

    def binary_search():
        l = 0
        r = 10 ** 9 + 1
        while r - l > 1:
            m = (l + r) // 2
            if can_buy(m):
                l = m
            else:
                r = m
        return l

    print(binary_search())

=======
Suggestion 9

def d(n):
    return len(str(n))

import sys
A,B,X = map(int,sys.stdin.readline().strip().split())
#print(A,B,X)
#A,B,X = map(int,"1234 56789 314159265".strip().split())
#print(A,B,X)

l = 0
r = 10**9
while l<r:
    m = (l+r+1)//2
    if A*m+B*d(m)<=X:
        l = m
    else:
        r = m-1
print(l)

=======
Suggestion 10

def get_digits(n):
    return len(str(n))
