Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i * i != n:
                print(n // i)
        i += 1

=======
Suggestion 2

def main():
    n = int(input())
    i = 1
    while i*i <= n:
        if n % i == 0:
            print(i)
            if i*i != n:
                print(n//i)
        i += 1
    return

=======
Suggestion 3

def divisors(n):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    return divs

n = int(input())
divs = divisors(n)
divs.sort()
for i in divs:
    print(i)

=======
Suggestion 4

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

N = int(raw_input())
f = sorted(list(factors(N)))
for i in f:
    print i

=======
Suggestion 5

def main():
    n = int(input())
    i = 1
    while i**2 <= n:
        if n % i == 0:
            print(i)
            if i**2 != n:
                print(n//i)
        i += 1

=======
Suggestion 6

def get_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if num // i != i:
                divisors.append(num//i)
    divisors.sort()
    return divisors

=======
Suggestion 7

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0)))
n = int(raw_input())
f = factors(n)
for i in sorted(f):
    print i

=======
Suggestion 8

def main():
    n = int(input())
    l = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            l.append(i)
            if i != n // i:
                l.append(n // i)
    l.sort()
    print(*l, sep='\n')

=======
Suggestion 9

def get_divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    table.sort()
    return table

n = int(input())

table = get_divisor(n)

for i in table:
    print(i)

=======
Suggestion 10

def get_divisors(n):
    divisors = []
    divisors_back = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors_back.append(n//i)
    return divisors + divisors_back[::-1]

N = int(input())
divisors = get_divisors(N)
for divisor in divisors:
    print(divisor)
