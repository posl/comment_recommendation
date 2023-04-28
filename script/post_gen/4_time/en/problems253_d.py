Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    total = 0
    for i in range(1, n + 1):
        if i % a != 0 and i % b != 0:
            total += i
    print(total)

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    print(sum([i for i in range(1, n+1) if i % a != 0 and i % b != 0]))

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, A, B = map(int, input().split())
g = gcd(A, B)
lcm = A * B // g

ans = N - (N // A + N // B - N // lcm)

print(ans)

=======
Suggestion 6

def sum_of_integers(N, A, B):
    sum = 0
    for i in range(1, N+1):
        if not (i % A == 0 or i % B == 0):
            sum += i
    return sum
