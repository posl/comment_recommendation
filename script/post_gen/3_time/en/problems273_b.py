Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, k = map(int, input().split())
    for i in range(1, k+1):
        x = round(x, -i)
    print(x)

=======
Suggestion 2

def main():
    x, k = map(int, input().split())
    print((x + 5 * 10 ** (k - 1)) // 10 ** k * 10 ** k)

=======
Suggestion 3

def main():
    X, K = [int(x) for x in input().split()]
    for i in range(1, K+1):
        X = round(X, -i)
    print(X)

=======
Suggestion 4

def main():
    x, k = map(int, input().split())
    for i in range(k):
        x = round(x, -i)
    print(x)

=======
Suggestion 5

def roundoff(x, k):
    for i in range(1, k+1):
        x = int(x / (10**i)) * (10**i)
    return x

x, k = map(int, input().split())
print(roundoff(x, k))

=======
Suggestion 6

def main():
    x, k = map(int, input().split())
    #print(x, k)
    for i in range(1, k+1):
        y = round(x, -i)
        #print(y)
        x = y
    print(x)

=======
Suggestion 7

def main():
    x,k = map(int,input().split())
    print(x+10**k-1-(x+10**k-1)%(10**k))

=======
Suggestion 8

def roundoff(x):
    if x % 1000 == 0:
        return x
    else:
        return (x // 1000 + 1) * 1000

=======
Suggestion 9

def nearestTen(x, i):
    return int(x/(10**i)+0.5)*(10**i)
