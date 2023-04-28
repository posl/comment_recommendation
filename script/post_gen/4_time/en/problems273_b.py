Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % 10 == 0:
            x = x // 10
        else:
            x = x - 1
    print(x)

=======
Suggestion 2

def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = (X // 10) * 10 if X % 10 < 5 else (X // 10 + 1) * 10
    print(X)

=======
Suggestion 3

def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = (X + 5) // 10 * 10
        if X == 0:
            break
    print(X)

=======
Suggestion 4

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

x, k = map(int, input().split())
for i in range(k):
    x = round_up(x, -i-1)
print(int(x))

=======
Suggestion 5

def rounding(x, k):
    for i in range(k):
        if x % (10**(i+1)) <= 5 * 10**i:
            x -= x % (10**(i+1))
        else:
            x += 10**(i+1) - x % (10**(i+1))
    return x

x, k = map(int, input().split())
print(rounding(x, k))

=======
Suggestion 6

def round_up(num, unit):
    if num % unit == 0:
        return num
    else:
        return (num // unit + 1) * unit

x, k = map(int, input().split())

for i in range(k):
    x = round_up(x, 10 ** (k - i))

print(x)

=======
Suggestion 7

def round(num, n):
    if num % (10 ** n) == 0:
        return num
    else:
        return round(num + 10 ** n - num % (10 ** n), n)


x, k = map(int, input().split())

print(round(x, k))

=======
Suggestion 8

def calc(X,K):
    if X==0:
        return 0
    else:
        return int(str(X)[0:K]+'0'*(len(str(X))-K))

X,K = [int(i) for i in input().split()]

print(calc(X,K))

=======
Suggestion 9

def round_off(number, i):
    return number + 5 * 10 ** (i - 1)
