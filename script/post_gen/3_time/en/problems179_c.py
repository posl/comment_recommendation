Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for A in range(1, N + 1):
        for B in range(1, N // A + 1):
            C = N - A * B
            if C > 0:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += (N - 1) // i
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += (N - 1) // i
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
    ans = 0
    for a in range(1, N):
        ans += (N - 1) // a
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N//i+1):
            if i * j + j == N:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N):
        cnt += (N - 1) // i
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    result = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (i*j + j) == N:
                result += 1
    print(result)
