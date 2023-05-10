Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    while len(a) > 1:
        m = a[0]
        for i in range(1, len(a)):
            m %= a[i]
            if m == 0:
                break
        if m == 0:
            a.pop(0)
        else:
            break
    print(a[0])

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
print(g)

=======
Suggestion 3

def attack(a,b):
    return a-b

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    while len(A) != 1:
        A.sort()
        x = A[0]
        y = A[1]
        if x == y:
            A = A[2:]
        else:
            A = A[2:] + [y-x]
    print(A[0])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    while len(a) > 1:
        a.sort()
        a[0] = a[0] % a[1]
        if a[0] == 0:
            a.pop(0)
    print(a[0])

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    while len(a) > 1:
        a.sort()
        a[-1] %= a[0]
        if a[-1] == 0:
            a.pop()
    print(a[0])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(min(A))
    else:
        print(1)

=======
Suggestion 9

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 10

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
