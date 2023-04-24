Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 3

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    print("Yes" if H <= sum(A) else "No")

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 6

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if h <= max(a):
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 8

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
Suggestion 9

def main():
    #input
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    #output
    if H <= sum(A):
        print('Yes')
    else:
        print('No')
