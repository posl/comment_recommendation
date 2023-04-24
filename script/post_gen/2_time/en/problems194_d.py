Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += (n / i) * (1 / n)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += i * (N / i)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    
    ans = 0
    for i in range(1, N):
        ans += (N / i)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    print(N + (N - 1) / 2)

=======
Suggestion 5

def main():
    n = int(input())
    print(sum([i * (1/n)**i for i in range(1, n+1)]))

=======
Suggestion 6

def main():
    n = int(input())
    print(n * (n + 1) / 2 / n)

=======
Suggestion 7

def main():
    n = int(input())
    print(n + (n-1)/2)

=======
Suggestion 8

def main():
    N = int(input())
    print((2*N-1)/N)

=======
Suggestion 9

def main():
    # Read input
    N = int(input())
    # Define variables
    # Calculate
    ans = 0
    for i in range(1,N):
        ans += N/(N-i)
    # Output
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    print(2*n - 1 - 1/n)
