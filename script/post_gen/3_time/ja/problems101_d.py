Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    ans = []
    n = 1
    while len(ans) < K:
        if n % sum(map(int, str(n))) == 0:
            ans.append(n)
        n += 1
    for a in ans:
        print(a)

=======
Suggestion 2

def main():
    K = int(input())
    ans = []
    i = 1
    while len(ans) < K:
        sum = 0
        for j in str(i):
            sum += int(j)
        if i / sum >= (i + 1) / (sum + 1):
            ans.append(i)
        i += 1
    for i in ans:
        print(i)

=======
Suggestion 3

def main():
    K = int(input())
    ans = []
    for i in range(1, 10):
        ans.append(i)
    for i in range(10, 10**15):
        if i % sum(map(int, str(i))) == 0:
            ans.append(i)
        if len(ans) > K:
            break
    for i in range(K):
        print(ans[i])

=======
Suggestion 4

def s(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 5

def S(n):
    return sum([int(x) for x in str(n)])

=======
Suggestion 6

def sum_digits(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 7

def sum_digits(n):
    return sum([int(d) for d in str(n)])

=======
Suggestion 8

def sum_of_digits(n):
    return sum(int(c) for c in str(n))

=======
Suggestion 9

def sumOfDigits(n):
    return sum([int(x) for x in str(n)])

=======
Suggestion 10

def sumDigit(n):
    return sum([int(i) for i in str(n)])
