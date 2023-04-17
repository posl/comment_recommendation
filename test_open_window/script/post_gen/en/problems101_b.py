Synthesizing 10/10 solutions

=======

def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======

def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

n = int(input())

=======

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum

=======

def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

=======

def main():
    N = int(input())
    S = sum(map(int, str(N)))
    if N % S == 0:
        print('Yes')
    else:
        print('No')

=======

def main():
    n = int(input())
    s = sum(int(d) for d in str(n))
    print('Yes' if n % s == 0 else 'No')

=======

def sum_digits(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

=======

def sum_digits(n):
    return sum(int(d) for d in str(n))

=======

def sum_of_digits(n):
    return sum(map(int, str(n)))

=======

def sum_digits(n):
    return sum(map(int, str(n)))
