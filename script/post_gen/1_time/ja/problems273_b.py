Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = X // (10 ** i) * (10 ** i) + round((X % (10 ** i)) / (10 ** i)) * (10 ** i)
    print(X)

=======
Suggestion 2

def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = round(X, -i)
    print(X)

=======
Suggestion 3

def main():
    X, K = map(int, input().split())
    print(X - X % (10 ** K) + (10 ** K if X % (10 ** K) >= (10 ** K) / 2 else 0))

=======
Suggestion 4

def round(x, k):
    for i in range(k):
        x = (x + 10 ** i - 1) // (10 ** i) * (10 ** i)
    return x

x, k = map(int, input().split())
print(round(x, k))

=======
Suggestion 5

def main():
    X, K = map(int, input().split())
    for i in range(K):
        Y = X // 10 ** (i + 1)
        if X % 10 ** (i + 1) >= 5 * 10 ** i:
            Y += 1
        X = Y * 10 ** (i + 1)
    print(X)

=======
Suggestion 6

def main():
    X, K = map(int, input().split())
    for i in range(K):
        Y = X // (10 ** i) * (10 ** i) + (10 ** i) // 2
        if Y % (10 ** (i + 1)) == 0:
            X = Y // (10 ** (i + 1)) * (10 ** (i + 1))
        else:
            X = Y // (10 ** (i + 1)) * (10 ** (i + 1)) + (10 ** (i + 1))
    print(X)

=======
Suggestion 7

def round_down(num, divisor):
    return num - (num%divisor)

=======
Suggestion 8

def main():
    x, k = map(int, input().split())
    #print(x, k)
    k = 10 ** k
    #print(k)
    x = x // k * k
    #print(x)
    x = x + k
    #print(x)
    x = x // k * k
    #print(x)
    print(x)
