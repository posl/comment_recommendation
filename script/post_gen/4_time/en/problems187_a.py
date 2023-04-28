Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 2

def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

a, b = map(int, input().split())
print(max(sum_of_digits(a), sum_of_digits(b)))

=======
Suggestion 3

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

a, b = [int(x) for x in input().split()]
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(max(sum(map(int, str(a))), sum(map(int, str(b)))))

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print(max(sum(map(int, str(A))), sum(map(int, str(B)))))

=======
Suggestion 6

def sum_digits(integer):
    sum = 0
    while integer:
        sum += integer % 10
        integer //= 10
    return sum

a, b = map(int, input().split())

=======
Suggestion 7

def main():
    a,b = input().split()
    sa = sum([int(i) for i in a])
    sb = sum([int(i) for i in b])
    print(max(sa,sb))
