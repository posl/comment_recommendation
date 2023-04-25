Synthesizing 10/10 solutions

=======
Suggestion 1

def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 2

def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 3

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 4

def S(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 5

def getSum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 6

def main():
    K = int(input())
    S = [0] * 10
    for i in range(1, 10):
        S[i] = i
    for i in range(1, 10):
        for j in range(1, 10):
            if (i * 10 + j) > 10 ** 15:
                break
            S.append(i * 10 + j)
            if len(S) == K + 1:
                break
    S.sort()
    for i in range(1, K + 1):
        print(S[i])

main()

=======
Suggestion 7

def sum_digits(n):
    return sum([int(x) for x in str(n)])

=======
Suggestion 8

def sum_digits(n):
    return sum(map(int, list(str(n))))

=======
Suggestion 9

def sum_digits(n):
    return sum(map(int, str(n)))

=======
Suggestion 10

def snuke(k):
    def sum_digits(n):
        return sum([int(x) for x in str(n)])

    def snuke_gen():
        yield 1
        for i in range(2, 10**15):
            if i % sum_digits(i) == 0:
                yield i

    return list(itertools.islice(snuke_gen(), k))
