Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 2

def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 3

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 4

def S(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 5

def S(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

K = int(input())
count = 0
n = 0
while count < K:
    n += 1
    if n/S(n) >= n/S(n+1):
        count += 1
        print(n)

=======
Suggestion 6

def S(n):
    return sum([int(i) for i in str(n)])

K = int(input())
n = 1
while K > 0:
    if n/S(n) <= (n+1)/S(n+1):
        print(n)
        K -= 1
    n += 1

=======
Suggestion 7

def s(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 8

def S(n):
    return sum([int(d) for d in str(n)])

=======
Suggestion 9

def main():
    K = int(input())
    print("\n".join(map(str, [i for i in range(1,K+1)])))
