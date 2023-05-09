Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % 10 == 0:
            x //= 10
        else:
            x -= 1
    print(x)

=======
Suggestion 2

def problems273_b():
    x, k = map(int, input().split())
    for i in range(k):
        if x % 10 == 0:
            x = x // 10
        else:
            x -= 1
    print(x)

=======
Suggestion 3

def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = (X + 5) // 10 * 10
    print(X)

=======
Suggestion 4

def problem273_b():
    x,k = map(int,input().split())
    for i in range(k):
        if x % 200 == 0:
            x = x // 200
        else:
            x = x * 1000 + 200
    print(x)

=======
Suggestion 5

def main():
    X,K = map(int,input().split())
    for i in range(K):
        X = (X // 10) * 10 if X % 10 < 5 else (X // 10 + 1) * 10
    print(X)

=======
Suggestion 6

def round_up(x, y):
    if x % y == 0:
        return x
    else:
        return x + y - x % y

x, k = map(int, input().split())

for i in range(k):
    x = round_up(x, 10**(k-i))

print(x)

=======
Suggestion 7

def round_x(x, k):
    for i in range(k):
        if x % 10 != 0:
            x += 10 - (x % 10)
        else:
            x //= 10
    return x

=======
Suggestion 8

def roundoff(x, k):
    for i in range(k):
        if x%10 == 0:
            x = x/10
        else:
            x = x - x%10 + 10
    return int(x)

x, k = map(int, input().split())
print(roundoff(x, k))

=======
Suggestion 9

def my_round(x, y):
    if x % y == 0:
        return x
    else:
        return int(x/y) * y + y

=======
Suggestion 10

def round_up(x, y):
    return x + y - x % y
