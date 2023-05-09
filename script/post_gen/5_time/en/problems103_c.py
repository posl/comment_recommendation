Synthesizing 10/10 solutions

=======
Suggestion 1

def f(m, a):
    sum = 0
    for i in range(len(a)):
        sum += m % a[i]
    return sum

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max([sum([a % A[i] for a in A]) for i in range(N)]))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max([sum([x % i for x in a]) for i in range(1, 1001)]))

=======
Suggestion 4

def f(m):
    return sum(m % a for a in A)

N = int(input())
A = list(map(int, input().split()))

l = 0
r = 10**9+1
while r - l > 1:
    m = (r + l) // 2
    if f(m) < f(m+1):
        r = m
    else:
        l = m

print(f(r))

=======
Suggestion 5

def f(m):
    return sum([m % a for a in A])

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    for i in range(N):
        a[i] = a[i] % a[0]
    #print(a)
    print(sum(a))

=======
Suggestion 7

def f(m, a):
    return sum([m % i for i in a])

n = int(input())
a = list(map(int, input().split()))
a.sort()
max_a = a[-1]
min_a = a[0]
max_f = 0

for i in range(min_a, max_a + 1):
    max_f = max(max_f, f(i, a))

print(max_f)

=======
Suggestion 8

def f(m, a):
    return sum(m % i for i in a)

N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

l = 0
r = 10**18

while r - l > 1:
    m = (l + r) // 2
    if f(m, a) >= f(m + 1, a):
        r = m
    else:
        l = m

print(f(r, a))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(sum(a)-n)

=======
Suggestion 10

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    #print(sum(a[:-1]))
    print(sum(a[:-1]) + a[-1] - 1)
