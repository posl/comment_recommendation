Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ans += 1
            if N / i != i:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0 and (n // i - 1) % 2 == 0:
                ans += 1
            if (n // i) % 2 == 0 and (i - 1) % 2 == 0:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            continue
        if N % i == 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if i * (i + 1) // 2 > N:
            break
        if (N - i * (i + 1) // 2) % i == 0:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if N%i == 0:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i%2 == 1 and N%i == 0:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for k in range(1, N+1):
        if N % k == 0:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if (N-i+1) % i == 0:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if N % i == 0:
            ans += N // i
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if N % i == 0:
            ans += (N//i - i + 1) // 2
    print(ans)
