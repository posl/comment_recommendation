Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    sum = 0
    for i in range(len(str(N))):
        sum += int(str(N)[i])
    if N % sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

n = int(input())

=======
Suggestion 3

def S(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

N = int(input())

=======
Suggestion 4

def S(n):
    if n < 10:
        return n
    else:
        return n % 10 + S(n // 10)

N = int(input())

=======
Suggestion 5

def sum_of_digits(n):
    return sum([int(x) for x in str(n)])

=======
Suggestion 6

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 7

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

N = int(input())
print("Yes" if N % sum_digits(N) == 0 else "No")

=======
Suggestion 8

def S(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n / 10
    return sum

n = int(raw_input())

=======
Suggestion 9

def S(n):
    sum=0
    while n!=0:
        sum+=n%10
        n=n//10
    return sum

N=int(input())

=======
Suggestion 10

def s(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum
