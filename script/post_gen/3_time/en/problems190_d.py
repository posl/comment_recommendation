Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N ** 0.5) + 1):
        if (N - i) % i == 0:
            ans += 1
    print(ans * 2 - 1)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            if i % 2 == 1:
                ans += 1
            if N // i % 2 == 1:
                ans += 1
            if i * i == N:
                ans -= 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            if i%2 == 1:
                ans += 1
            if N//i%2 == 1:
                ans += 1
            if i**2 == N:
                ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            ans += 2
        if i*i == N:
            ans -= 1
    print(ans)

=======
Suggestion 5

def solve(n):
    ans = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            ans += 1
            if i*i != n:
                ans += 1
    return ans

n = int(input())
print(solve(n))

=======
Suggestion 6

def solve(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 2
            if i * i == n:
                count -= 1
    return count

n = int(input())
print(solve(n))

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N % i == 0 and N // i - i >= 0:
            ans += 2
        if N % i == 0 and N // i - i == 1:
            ans -= 1
    print(ans)

=======
Suggestion 8

def num_of_arithmetic_progressions(n):
    result = 0
    for i in range(1, n+1):
        if (n-i) % i == 0:
            result += 1
    return result

n = int(input())
print(num_of_arithmetic_progressions(n))

=======
Suggestion 9

def sum_of_progression(a1, an, n):
    return (a1 + an) * n // 2

=======
Suggestion 10

def main():
    N = int(input())
    print(N)
