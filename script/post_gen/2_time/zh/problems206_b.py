Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N = int(input())
    # x(x+1)/2 >= N
    # x^2 + x - 2N >= 0
    # x = (-1 + sqrt(1+8N))/2
    # x = (-1 - sqrt(1+8N))/2
    # x >= 0
    # -1 + sqrt(1+8N) >= 0
    # sqrt(1+8N) >= 1
    # 1+8N >= 1

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 3

def main():
    n = int(input())
    i = 1
    sum = 0
    while sum < n:
        sum += i
        i += 1
    print(i-1)

=======
Suggestion 4

def problem206_b():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += i
        if ans >= n:
            print(i)
            break

=======
Suggestion 5

def main():
    n = int(input())
    s = 0
    for i in range(1, n+1):
        s += i
        if s >= n:
            print(i)
            break

=======
Suggestion 6

def main():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        sum += i
        if sum >= N:
            print(i)
            break

=======
Suggestion 7

def main():
    n = int(input())
    x = 0
    for i in range(1, n + 1):
        x += i
        if x >= n:
            print(i)
            break

=======
Suggestion 8

def main():
    N = int(input())
    x = 0
    while True:
        x += 1
        if x * (x + 1) / 2 >= N:
            break
    print(x)

main()
