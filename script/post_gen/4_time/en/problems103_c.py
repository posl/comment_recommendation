Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i] - 1
    print(sum)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = a[0]
    for i in range(1, n):
        m = min(m, a[i] - a[i - 1])
    print(m)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = a[0]
    for i in range(1, len(a)):
        m = m * a[i] // gcd(m, a[i])
    print(sum(m - 1 for a in a) % (10**9 + 7))

=======
Suggestion 4

def f(m):
    return sum(m % a for a in A)

N = int(input())
A = list(map(int, input().split()))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A) - N)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    m = a[0] - 1
    for i in range(1, len(a)):
        m -= a[i]
    print(m)

=======
Suggestion 7

def f(m, a):
    return sum([m % i for i in a])

N = int(input())
a = [int(i) for i in input().split()]

l = 0
r = 10 ** 9
while r - l > 1:
    m = (l + r) // 2
    if f(m, a) >= f(m + 1, a):
        r = m
    else:
        l = m

print(f(r, a))

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max = 0
    for i in range(N):
        max += a[i] * (N-i-1)
    print(max)

=======
Suggestion 9

def f(m, a):
    return sum([m % i for i in a])

n = int(input())
a = list(map(int, input().split()))

ok = 0
ng = 10**9 + 1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(mid, a) < f(mid + 1, a):
        ng = mid
    else:
        ok = mid

print(f(ok + 1, a))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    #print(A[-1])
    max_f = 0
    for m in range(0, A[-1]):
        #print(m)
        f = 0
        for i in range(0, N):
            f += m % A[i]
        #print(f)
        if f > max_f:
            max_f = f
    print(max_f)
