Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X,K = map(int,input().split())
    for i in range(K):
        X = (X + 5) // 10 * 10
    print(X)

main()

=======
Suggestion 2

def main():
    x,k = map(int, input().split())
    for i in range(k):
        if x % 10 == 0:
            x = x // 10
        else:
            x += 10 - (x % 10)
    print(x)

=======
Suggestion 3

def main():
    x,k = map(int,input().split())
    for i in range(k):
        x = ((x+5)//10)*10
    print(x)

=======
Suggestion 4

def get_digit(n):
    digit = 0
    while n > 0:
        n //= 10
        digit += 1
    return digit

X,K = map(int,input().split())
for _ in range(K):
    if X % 10 == 0:
        X //= 10
    else:
        X += 10 - X % 10
print(X)

=======
Suggestion 5

def problems273_b():
    x,k = map(int,input().split())
    for _ in range(k):
        if x%10 == 0:
            x //= 10
        else:
            x -= 1
    print(x)

=======
Suggestion 6

def rounding(x, k):
    for i in range(k):
        if x % 10 == 0:
            x //= 10
        else:
            x += 10 - (x % 10)
    return x

x, k = map(int, input().split())
print(rounding(x, k))

=======
Suggestion 7

def main():
    x, k = map(int, input().split())
    for i in range(k):
        x = (x + 5) // 10 * 10
    print(x)

=======
Suggestion 8

def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % 10 == 0:
            x //= 10
        else:
            x += 10 - x % 10
    print(x)

=======
Suggestion 9

def main():
    X,K = map(int,input().split())
    for i in range(K):
        X = (X+5)//10*10
    print(X)

=======
Suggestion 10

def main():
    X,K = map(int, input().split())
    for i in range(K):
        if X%10 == 0:
            X = X//10
        else:
            X += 10 - X%10
    print(X)
