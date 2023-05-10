Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if a * b + c == n:
                    ans += 1
    print(ans)

=======
Suggestion 2

def problem179_c():
    n = int(input())
    ans = 0
    for i in range(1, n):
        for j in range(1, int(n/i)):
            if i * j + i == n:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1,N):
        for j in range(1,N):
            for k in range(1,N):
                if i*j+k == N:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j < n:
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    count = 0
    for i in range(1,n):
        for j in range(1,n):
            if i*j >= n:
                break
            if (n-i*j)%j == 0:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    count = 0
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if a * b + c == n:
                    count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    count = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j < n:
                count += 1
            else:
                break
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    count = 0
    for i in range(1,N):
        tmp = N - i
        for j in range(1,tmp):
            if tmp % j == 0:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += (n - 1) // i
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a * b >= n:
                break
            if (n - a * b) % a == 0:
                count += 1
    print(count)
