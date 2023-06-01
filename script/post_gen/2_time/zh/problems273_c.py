Synthesizing 10/10 solutions

=======
Suggestion 1

def round_up(x, y):
    if x % y == 0:
        return x
    else:
        return x + y - x % y

=======
Suggestion 2

def main():
    x,k = map(int,input().split())
    if k == 0:
        print(x)
        return
    if x == 0:
        print(0)
        return
    if x < 10:
        print(10)
        return
    if x < 100:
        print(int(x/10)*10)
        return
    if x < 1000:
        print(int(x/100)*100)
        return
    if x < 10000:
        print(int(x/1000)*1000)
        return
    if x < 100000:
        print(int(x/10000)*10000)
        return
    if x < 1000000:
        print(int(x/100000)*100000)
        return
    if x < 10000000:
        print(int(x/1000000)*1000000)
        return
    if x < 100000000:
        print(int(x/10000000)*10000000)
        return
    if x < 1000000000:
        print(int(x/100000000)*100000000)
        return
    if x < 10000000000:
        print(int(x/1000000000)*1000000000)
        return
    if x < 100000000000:
        print(int(x/10000000000)*10000000000)
        return
    if x < 1000000000000:
        print(int(x/100000000000)*100000000000)
        return
    if x < 10000000000000:
        print(int(x/1000000000000)*1000000000000)
        return
    if x < 100000000000000:
        print(int(x/10000000000000)*10000000000000)
        return
    if x < 1000000000000000:
        print(int(x/100000000000000)*100000000000000)
        return
    if x < 10000000000000000:
        print(int(x/1000000000000000)*1000000000000000)
        return
    if x < 100000000000000000:
        print(int(x/10000000000000000)*10000000000000000)
        return
    if x < 1000000000000000000:
        print

=======
Suggestion 3

def round_up(x, k):
    if k == 0:
        return x
    else:
        a = round_up(x, k - 1)
        b = 10 ** k
        return (a + b - 1) // b * b

=======
Suggestion 4

def problems273_b():
    X,K = input().split()
    K = int(K)
    num = int(X)
    for i in range(K):
        num = round(num, -i-1)
    print(num)

=======
Suggestion 5

def round_up(x, i):
    if x % (10 ** i) >= 5 * 10 ** (i - 1):
        return x - x % (10 ** i) + 10 ** i
    else:
        return x - x % (10 ** i)

=======
Suggestion 6

def main():
    X,K = map(int, input().split())
    for i in range(1,K+1):
        if X%(10**i) < 5*(10**(i-1)):
            print((X//(10**i))*(10**i))
            break
        else:
            print((X//(10**i)+1)*(10**i))
            break

=======
Suggestion 7

def main():
    x, k = map(int,input().split())
    result = x
    for i in range(k):
        result = round(result, -i - 1)
    print(result)

=======
Suggestion 8

def main():
    x, k = map(int, input().split())
    for i in range(k):
        x = (x + 5) // 10 * 10
    print(x)

=======
Suggestion 9

def round_up(x, n):
    if n == 1:
        return x
    else:
        return (x // (10 ** n) + 1) * (10 ** n)

X, K = map(int, input().split())

for _ in range(K):
    X = round_up(X, K)

print(X)

=======
Suggestion 10

def main():
    x,k = map(int, input().split())
    #print(x,k)
    for i in range(k):
        if x % (10**(i+1)) < 5 * 10**i:
            print(x - x % (10**(i+1)))
            break
        else:
            print(x + (10**(i+1) - x % (10**(i+1))))
            break
