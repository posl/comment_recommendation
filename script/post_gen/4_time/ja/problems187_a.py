Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def S(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n = n // 10
    return ans

A, B = map(int, input().split())
print(max(S(A), S(B)))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(max(sum(map(int, str(a))), sum(map(int, str(b)))))

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    print(max(sum([int(i) for i in str(a)]), sum([int(i) for i in str(b)])))

=======
Suggestion 4

def solve():
    a, b = map(int, input().split())
    print(max(sum([int(c) for c in str(a)]), sum([int(c) for c in str(b)])))

=======
Suggestion 5

def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum


a, b = map(int, input().split())

print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 6

def sum_digits(num):
    return sum([int(i) for i in str(num)])

A, B = map(int, input().split())
print(max(sum_digits(A), sum_digits(B)))

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    a = sum(list(map(int,str(a))))
    b = sum(list(map(int,str(b))))
    print(a if a>b else b)

=======
Suggestion 8

def sum_digits(number):
    return sum([int(digit) for digit in str(number)])

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))
