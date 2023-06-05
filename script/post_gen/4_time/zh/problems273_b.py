Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, k = map(int, input().split())
    for i in range(k):
        x = (x + 10 ** i) // (10 ** i) * (10 ** i)
    print(x)

=======
Suggestion 2

def main():
    x,k = map(int,input().split())
    x = int(x)
    k = int(k)
    for i in range(k):
        if x % (10 ** (i + 1)) >= 5 * 10 ** i:
            x = (x // (10 ** (i + 1)) + 1) * (10 ** (i + 1))
        else:
            x = (x // (10 ** (i + 1))) * (10 ** (i + 1))
    print(x)

=======
Suggestion 3

def problem273_b():
    x,k = map(int,input().split())
    ans = x
    for i in range(k):
        ans = (ans+5)//10*10
    print(ans)

=======
Suggestion 4

def round_up(x, k):
    if k == 0:
        return x
    if x == 0:
        return 0
    if x % (10 ** k) == 0:
        return x
    else:
        return round_up(x + 10 ** k - x % (10 ** k), k)

=======
Suggestion 5

def main():
    x, k = map(int, input().split())
    y = x
    for i in range(k):
        if y % (10 ** (i + 1)) >= 5 * (10 ** i):
            y = y // (10 ** (i + 1)) * (10 ** (i + 1)) + (10 ** (i + 1))
        else:
            y = y // (10 ** (i + 1)) * (10 ** (i + 1))
    print(y)

=======
Suggestion 6

def main():
    x,k = map(int,input().split())
    result = x
    for i in range(k):
        result = (result//10)*10
        if x%10 >= 5:
            result += 10
        x = result
    print(result)

=======
Suggestion 7

def main():
    X,K = map(int,input().split())
    for i in range(K):
        if X%10 == 0:
            X = X//10
        else:
            X = X - X%10 + 10
    print(X)

=======
Suggestion 8

def problems273_b():
    x,k = map(int,input().split())
    for i in range(k):
        if x%10!=0:
            x+=10-x%10
    print(x)

=======
Suggestion 9

def round_off(x,k):
    if k == 0:
        return x
    else:
        return round_off(x//10,k-1)*10**k if x%10**k >= 5*10**(k-1) else round_off(x//10,k-1)*10**k+5*10**(k-1)

x,k = map(int,input().split())
print(round_off(x,k))
