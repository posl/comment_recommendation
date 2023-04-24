Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, K = map(int, input().split())
    for i in range(K):
        if X % 10 == 0:
            X //= 10
        else:
            X -= 1
    print(X)

=======
Suggestion 2

def main():
    x,k = map(int,input().split())
    for i in range(k):
        if x % 10 == 0:
            x = x // 10
        else:
            x = x - 1
    print(x)

=======
Suggestion 3

def main():
    x,k = map(int, input().split())
    for i in range(k):
        if x % 10 == 0:
            x /= 10
        else:
            x -= 1
    print(int(x))

=======
Suggestion 4

def solve():
    X, K = map(int, input().split())
    for i in range(K):
        if X % 10 == 0:
            X //= 10
        else:
            X -= 1
    print(X)
solve()

=======
Suggestion 5

def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % (10 ** (k - i)) == 0:
            print(x)
            break
        else:
            x = x + (10 ** (k - i))
    else:
        print(x)

=======
Suggestion 6

def round(x, k):
    for i in range(k):
        if x % 10 != 0:
            x = x + 10 - (x % 10)
        else:
            x = x // 10
    return x

x, k = map(int, input().split())
print(round(x, k))

=======
Suggestion 7

def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % (10**(i+1)) <= 10**i:
            x = x - x % (10**(i+1))
        else:
            x = x - x % (10**(i+1)) + 10**(i+1)
    print(x)

=======
Suggestion 8

def round_off(x, k):
    for i in range(1, k+1):
        x = round(x, -i)
    return x

=======
Suggestion 9

def round_up_to_10_power_i(x, i):
    if i == 0:
        return x
    if x % (10**i) == 0:
        return x
    return x + (10**i - x % (10**i))

x, k = map(int, input().split())
for i in range(k):
    x = round_up_to_10_power_i(x, i)
print(x)

=======
Suggestion 10

def round_of_n(num, n):
    num = str(num)
    if len(num) > n:
        return int(num[:-n] + '0' * n)
    else:
        return 0
