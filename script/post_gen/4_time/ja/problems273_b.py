Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, K = map(int, input().split())
    for i in range(K):
        if X % 10 == 0:
            X = X // 10
        else:
            X -= 1
    print(X)

=======
Suggestion 2

def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % (10 ** (i + 1)) >= 5 * (10 ** i):
            x += 10 ** (i + 1) - x % (10 ** (i + 1))
        else:
            x -= x % (10 ** (i + 1))
    print(x)

=======
Suggestion 3

def main():
    x,k = map(int, input().split())
    for i in range(k):
        if x%10 != 0:
            x += 10 - x%10
        else:
            x //= 10
    print(x)

=======
Suggestion 4

def main():
    x,k = map(int,input().split())
    for i in range(k):
        if x % (10**(k-i)) < 5*(10**(k-i-1)):
            x = x - (x % (10**(k-i)))
        else:
            x = x + (10**(k-i)) - (x % (10**(k-i)))
    print(x)

=======
Suggestion 5

def main():
    X,K = map(int,input().split())
    for i in range(K):
        if X%10 == 0:
            X = X//10
        else:
            X = X - X%10 + 10
    print(X)

=======
Suggestion 6

def main():
    X, K = map(int, input().split())
    for i in range(K):
        if X % pow(10, i+1) < pow(10, i+1) // 2:
            X = X - X % pow(10, i+1)
        else:
            X = X - X % pow(10, i+1) + pow(10, i+1)
    print(X)

=======
Suggestion 7

def solve():
    X,K = map(int,input().split())
    for i in range(K):
        if X % 10 != 0:
            X += 5 - (X % 10) if X % 10 < 5 else 10 - (X % 10)
        else:
            X //= 10
    print(X)

=======
Suggestion 8

def solve():
    X,K = map(int,input().split())
    for i in range(K):
        if i == K-1:
            break
        if X % (10**(K-i)) >= 5*(10**(K-i-1)):
            X = X + (10**(K-i)) - (X % (10**(K-i)))
        else:
            X = X - (X % (10**(K-i)))
    print(X)
    return 0

=======
Suggestion 9

def main():
    X, K = map(int, input().split())
    for i in range(K):
        if X % 10 ** i != 0:
            X = X // 10 ** i * 10 ** i
        else:
            continue
    print(X)

=======
Suggestion 10

def roundUp(x):
    if x%10>=5:
        return x + 10 - x%10
    else:
        return x - x%10
