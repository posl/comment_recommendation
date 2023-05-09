Synthesizing 10/10 solutions

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

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

n = int(input())

=======
Suggestion 3

def main():
    N = input()
    S = 0
    for i in N:
        S += int(i)
    if int(N) % S == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s

=======
Suggestion 5

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

N = int(input())
print("Yes" if N % S(N) == 0 else "No")

=======
Suggestion 6

def s(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

n = int(input())

=======
Suggestion 7

def main():
    n = int(input())
    s = sum(map(int, str(n)))
    if n % s == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def S(n):
    n_str = str(n)
    sum = 0
    for i in range(len(n_str)):
        sum += int(n_str[i])
    return sum

=======
Suggestion 9

def S(n):
    return sum([int(x) for x in str(n)])

=======
Suggestion 10

def sum_of_digits(n):
    return sum([int(x) for x in str(n)])
