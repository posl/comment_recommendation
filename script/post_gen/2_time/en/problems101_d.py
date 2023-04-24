Synthesizing 10/10 solutions

=======
Suggestion 1

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 2

def main():
    K = int(input())
    ans = []
    for i in range(1, 10):
        ans.append(i)
    for i in range(10, 10 ** 15):
        if i % sum(map(int, list(str(i)))) == 0:
            ans.append(i)
        if len(ans) == K:
            break
    for i in ans:
        print(i)

=======
Suggestion 3

def snuke():
    K = int(input())
    snuke_numbers = [1]
    for i in range(K):
        print(snuke_numbers[i])
        snuke_numbers.append(snuke_numbers[i] * 10)
        snuke_numbers.append(snuke_numbers[i] * 10 + 1)
        snuke_numbers.sort()

=======
Suggestion 4

def sum_digits(n):
    return sum([int(d) for d in str(n)])

=======
Suggestion 5

def sum_digits(n):
    return sum(int(d) for d in str(n))

=======
Suggestion 6

def S(n):
    return sum(int(d) for d in str(n))

=======
Suggestion 7

def snuke_numbers(k):
    s = 0
    for i in range(1, k + 1):
        s += i
        if s > 9:
            s = s % 9
        if s == 1 or s == 3 or s == 6 or s == 8:
            print(i)

=======
Suggestion 8

def S(n):
    return sum(map(int, str(n)))

=======
Suggestion 9

def sum_digits(n):
    return sum(map(int, str(n)))

=======
Suggestion 10

def s(n):
    return sum(map(int, list(str(n))))
