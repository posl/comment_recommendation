Synthesizing 10/10 solutions

=======
Suggestion 1

def round_up(x, y):
    z = x
    for i in range(y):
        if z % 10 == 0:
            break
        z += 1
    return z

x, k = map(int, input().split())
print(round_up(x, k))

=======
Suggestion 2

def main():
    x,k = map(int,input().split())
    i = 0
    while i < k:
        x = x + 5 - x % 10 if x % (10 ** (i + 1)) >= 5 * 10 ** i else x - x % 10
        i += 1
    print(x)

=======
Suggestion 3

def problem273_b(x, k):
    y = x
    for i in range(k):
        y = round(y, -i)
    print(int(y))


problem273_b(2048, 2)
problem273_b(1, 15)
problem273_b(999, 3)
problem273_b(314159265358979, 12)

=======
Suggestion 4

def round_up(num, i):
    if num % (10 ** i) == 0:
        return num
    else:
        return num + (10 ** i - num % (10 ** i))

=======
Suggestion 5

def round_up(x, y):
    if x % y == 0:
        return x
    else:
        return x + y - x % y

=======
Suggestion 6

def main():
    x,k=map(int,input().split())
    ans=x
    for i in range(k):
        ans=(ans+5)//10*10
    print(ans)

=======
Suggestion 7

def problems273_b():
    x,k = map(int,input().split())
    for i in range(k):
        x = (x+5)//10*10
        if x%10 == 0:
            x = x//10
    print(x)

=======
Suggestion 8

def problem273_b(x, k):
    if k == 0:
        return x
    if x % (10 ** k) == 0:
        return x
    else:
        return x - x % (10 ** k) + 10 ** k

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    print((a + (10 ** b - a % (10 ** b)) % (10 ** b)) % (10 ** b))

=======
Suggestion 10

def main():
    x,k = map(int,input().split())
    for i in range(k):
        x = (x+5)//10*10
    print(x)
