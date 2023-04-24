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

A, B = map(int, input().split())
print(max(sum_digits(A), sum_digits(B)))

=======
Suggestion 3

def sum_digits(num):
    s = 0
    while num:
        s += num % 10
        num //= 10
    return s

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 4

def main():
    a, b = [int(x) for x in input().split()]
    print(max(sum([int(x) for x in str(a)]), sum([int(x) for x in str(b)])))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(max(sum(map(int, str(a))), sum(map(int, str(b)))))

=======
Suggestion 6

def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    print(max(sum(map(int, str(A))), sum(map(int, str(B)))))

=======
Suggestion 7

def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

A, B = map(int, input().split())

=======
Suggestion 8

def sum_of_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum

a, b = map(int, input().split())
print(max(sum_of_digits(a), sum_of_digits(b)))

=======
Suggestion 9

def main():
    # input
    A, B = map(int, input().split())

    # compute
    S_A = A//100 + (A%100)//10 + A%10
    S_B = B//100 + (B%100)//10 + B%10

    # output
    print(max(S_A, S_B))

=======
Suggestion 10

def main():
    a,b = input().split()
    a = list(a)
    b = list(b)
    print(max(sum(map(int, a)), sum(map(int, b))))
