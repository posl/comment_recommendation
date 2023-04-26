Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            c = N - a * b
            if c < 1:
                break
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += (N - 1) // i
    print(ans)

main()

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for a in range(1, N):
        ans += (N - 1) // a
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for A in range(1, N):
        ans += (N - 1) // A
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    count = 0
    for a in range(1, N):
        for b in range(1, N):
            c = N - a*b
            if c > 0:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for A in range(1, N):
        for B in range(1, N):
            if A * B < N:
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1,N):
        ans += (N-1)//i
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j + j <= N:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += N // i
    print(ans)

=======
Suggestion 10

def f(n):
    ans = 0
    for i in range(1, n):
        ans += (n - 1) // i
    return ans

n = int(input())
print(f(n))
