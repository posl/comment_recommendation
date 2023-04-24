Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += (N - 1) // i
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for A in range(1, N):
        ans += (N - 1) // A
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for A in range(1, N + 1):
        for B in range(1, N + 1):
            C = A * B
            if C > N:
                break
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        count += (N - 1) // i
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    count = 0
    for A in range(1, N+1):
        for B in range(1, N+1):
            C = A*B - N
            if C < 1:
                continue
            if C % A == 0:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += (N-1) // i
    print(ans)

=======
Suggestion 7

def sum_divisors(n):
    ans = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans += i
            if i != n // i:
                ans += n // i
    return ans

N = int(input())
print(sum_divisors(N) - N)

=======
Suggestion 8

def main():
    N = int(input())

    # N = A * B + C
    # A * B = N - C
    # A = (N - C) / B
    # A = (N - C) // B
    # A * B = (N - C) // B * B
    # A * B = N - C - (N - C) % B
    # A * B = C + (N - C) % B
    # C = A * B - (N - C) % B
    # C = A * B - N % B
    # C = A * B - (N - (N // B) * B)
    # C = A * B - (N - N + N
