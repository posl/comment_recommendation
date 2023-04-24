Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
    ans.sort()
    for a in ans:
        print(a)

=======
Suggestion 2

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            ans.append(N//i)
    ans.sort()
    for a in ans:
        print(a)

=======
Suggestion 3

def divisor(n):
    i = 1
    result = []
    while i*i <= n:
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n//i)
        i += 1
    return result

N = int(input())
divisors = divisor(N)
divisors.sort()
for d in divisors:
    print(d)

The input is an integer N (1≦N≦10^{12}).
The output is all possible number of people to which we can evenly distribute the cream puffs without cutting them.

The answer is the number of divisors of N.
I used the function divisor(n) to get the divisors of N.
The function divisor(n) returns the list of divisors of n.

=======
Suggestion 4

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 5

def main():
    n = int(input())
    ans = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n//i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            ans.append(i)
            ans.append(N // i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 7

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

n = int(input())
divisors = find_divisors(n)
divisors.sort()
for d in divisors:
    print(d)

=======
Suggestion 8

def main():
    from math import sqrt
    N = int(input())
    ans = []
    for i in range(1, int(sqrt(N))+1):
        if N % i == 0:
            ans.append(i)
            if N // i != i:
                ans.append(N // i)
    ans.sort()
    for i in ans:
        print(i)
