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
    for a in range(1, N):
        ans += (N - 1) // a
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for b in range(1, N):
        ans += (N - 1) // b
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    result = 0
    for a in range(1, N):
        result += (N - 1) // a
    print(result)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N//i+1):
            if N - i*j >= 0:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        cnt += (N-1) // i
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    result = 0
    for a in range(1, n):
        for b in range(1, n):
            result += (n - a * b) // a
    print(result)

=======
Suggestion 8

def main():
    N = int(input())
    count = 1
    for i in range(1, N):
        if i % 2 == 0:
            count += 1
    print(count)
