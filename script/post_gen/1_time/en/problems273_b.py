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

def main():
    X, K = map(int, input().split())
    for i in range(K):
        if X % 10 == 0:
            X = X // 10
        else:
            X -= 1
    print(X)

=======
Suggestion 3

def main():
    X, K = map(int, input().split())
    for i in range(K):
        if X%10 == 0:
            X = X//10
        else:
            X = X - 1
    print(X)

=======
Suggestion 4

def problems273_b():
    x,k = map(int, input().split())
    for i in range(k):
        if x % 10 == 0:
            x = x // 10
        else:
            x = x - 1
    print(x)

=======
Suggestion 5

def rounding(x, k):
    if k == 0:
        return x
    else:
        return rounding(round(x, -k), k-1)

x, k = map(int, input().split())
print(rounding(x, k))

=======
Suggestion 6

def problems273_b():
    x, k = map(int, input().split())
    for i in range(k):
        x = (x+5)//10*10
    print(x)

=======
Suggestion 7

def round_up(x, y):
    if x % y == 0:
        return x
    else:
        return (x // y + 1) * y

x, k = map(int, input().split())
for i in range(k):
    x = round_up(x, 10 ** (k - i))
print(x)

=======
Suggestion 8

def round_off(x, k):
    for i in range(k):
        if x % 10 != 0:
            x += 10 - x % 10
    return x

x, k = map(int, input().split())
print(round_off(x, k))

=======
Suggestion 9

def main():
    # Take input
    x, k = map(int, input().split())

    # Round off to the nearest 10^i
    for i in range(k):
        if x % 10 == 0:
            x //= 10
        else:
            x -= 1

    # Print the answer
    print(x)

=======
Suggestion 10

def nearest_10_pow(x, k):
    for i in range(k):
        if x % (10 ** (i+1)) == 0:
            continue
        else:
            x = x + 10 ** (i+1) - x % (10 ** (i+1))
    return x

x, k = map(int, input().split())

print(nearest_10_pow(x, k))
