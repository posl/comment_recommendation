Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

h, n = map(int, input().split())
a = list(map(int, input().split()))
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])

=======
Suggestion 4

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 5

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    print("Yes" if h <= sum(a) else "No")

=======
Suggestion 6

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= max(A):
        print("Yes")
    else:
        if H % min(A) == 0:
            print("No")
        else:
            print("Yes")

=======
Suggestion 7

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if h <= a[0]:
        print("Yes")
    else:
        print("No")
