Synthesizing 10/10 solutions

=======
Suggestion 1

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

n = int(raw_input().strip())
f = factors(n)
for i in sorted(f):
    print i

=======
Suggestion 2

def main():
    n = int(input())
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i != n // i:
                print(n // i)
        i += 1
    return

=======
Suggestion 3

def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if i != N // i:
                print(N // i)
        i += 1

=======
Suggestion 4

def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if N // i != i:
                print(N // i)
        i += 1

=======
Suggestion 5

def factors(n):
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0)))

n = int(raw_input())
for i in sorted(factors(n)):
    print i

=======
Suggestion 6

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
 
N = int(raw_input())
f = factors(N)
for i in sorted(f):
    print i

=======
Suggestion 7

def solve(N):
    i = 1
    ans = []
    while i * i <= N:
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
        i += 1
    ans.sort()
    return ans

N = int(input())
for i in solve(N):
    print(i)

=======
Suggestion 8

def main():
    n = int(input())
    l = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            l.append(i)
            if i != n//i:
                l.append(n//i)
    l.sort()
    for i in l:
        print(i)

=======
Suggestion 9

def factors(n):
    factors = []
    for i in range(1, n+1):
        if n%i == 0:
            factors.append(i)
    return factors

n = int(input())
f = factors(n)
for i in f:
    print(i)

=======
Suggestion 10

def main():
    N = int(input())
    N_sqrt = int(N**0.5)
    divisors = []
    for i in range(1, N_sqrt+1):
        if N % i == 0:
            print(i)
            if i != N // i:
                divisors.append(N // i)
    for i in reversed(divisors):
        print(i)
