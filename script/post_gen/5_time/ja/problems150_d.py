Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,M,A)
    X = []
    for a in A:
        #print(a)
        X.append(a//2)
    #print(X)
    #print(max(X))
    #max_X = max(X)
    #

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def lcm(a,b):
    return a*b//gcd(a,b)

=======
Suggestion 4

def gcd(a,b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = list(set(a))
    a.sort()
    a = a[::-1]
    a2 = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 4 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 8 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 16 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 32 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 64 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 128 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 256 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 512 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] % 1024 == 0:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] == 2:
            a2.append(a[i])
    a = a2
    a2 = []
    for i in range(len(a)):
        if a[i] == 4:
            a2.append(a[i])
    a = a2
    a

=======
Suggestion 7

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

import math
import collections

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

a = list(map(lambda x: x // 2, a))
a = list(map(lambda x: lcm(x, 1), a))
a = list(map(lambda x: x // 1, a))
a = list(map(lambda x: x // 2, a))
a = list(map(lambda x: x // 1, a))

c = collections.Counter(a)
c = sorted(c.items(), key=lambda x:x[0])
c = list(map(lambda x: x[1], c))

ans = 0
for i in range(1, m + 1):
    d = 0
    for j in c:
        if i % j == 0:
            d += 1
    if d == len(c):
        ans += 1

print(ans)
