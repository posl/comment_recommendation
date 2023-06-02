Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_digit(n):
    return len(str(n))

=======
Suggestion 2

def d(n):
    if n < 10:
        return 1
    else:
        return d(n//10) + 1

=======
Suggestion 3

def d(N):
    if N == 0:
        return 0
    else:
        return d(N//10)+1

A, B, X = map(int, input().split())

left = 0
right = 10**9+1

while right - left > 1:
    middle = (left + right)//2
    if A*middle + B*d(middle) <= X:
        left = middle
    else:
        right = middle

print(left)

=======
Suggestion 4

def d(n):
    return len(str(n))

=======
Suggestion 5

def f(A, B, X):
    if A + B > X:
        return 0
    elif A * 10 + B * 1 <= X:
        return 10
    else:
        for i in range(1, 10):
            if A * i + B * len(str(i)) > X:
                return i - 1
        return 0

=======
Suggestion 6

def d(n):
    if n < 10:
        return 1
    else:
        return d(n/10) + 1

=======
Suggestion 7

def d(n):
    if n < 10:
        return 1
    else:
        return 1 + d(n // 10)

=======
Suggestion 8

def d(n):
    if n < 10:
        return 1
    else:
        return 1 + d(n/10)

a,b,x = map(int,input().split())

left = 0
right = 10**9 + 1

while right - left > 1:
    mid = (left + right)//2
    if a*mid + b*d(mid) <= x:
        left = mid
    else:
        right = mid

print(left)
