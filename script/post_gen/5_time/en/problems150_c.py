Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def next_permutation(a):
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i+1]):
        i -= 1
    if i < 0:
        return False
    j = len(a) - 1
    while not (a[i] < a[j]):
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i+1:] = reversed(a[i+1:])
    return True

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

a = 0
b = 0
i = 0
while i < n:
    a += p[i] * (n ** i)
    b += q[i] * (n ** i)
    i += 1
print(abs(a - b))

=======
Suggestion 2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

=======
Suggestion 3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    a, b = 0, 0
    for i in range(N):
        a += P[i] * (N - i) * ((N - i) - 1) // 2
        b += Q[i] * (N - i) * ((N - i) - 1) // 2
    print(abs(a - b))

=======
Suggestion 5

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

=======
Suggestion 6

def permutations(n):
    if n == 1:
        yield [1]
    else:
        for p in permutations(n - 1):
            for i in range(n):
                yield p[:i] + [n] + p[i:]

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    print(abs(get_index(p, n) - get_index(q, n)))

=======
Suggestion 8

def permutation(n):
    if n == 0:
        return [[]]
    else:
        return [[x] + y for x in range(n) for y in permutation(n - 1) if x not in y]
