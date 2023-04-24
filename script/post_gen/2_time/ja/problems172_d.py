Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * (N // i) * ((N // i) + 1) // 2
    print(ans)

=======
Suggestion 2

def divisor_count(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * (N//i)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * f(i)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * len([x for x in range(1, i+1) if i % x == 0])
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += (N//i) * (N//i+1) * i // 2
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += i * (n // i)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    # 約数の個数を求める
    for i in range(1,N+1):
        ans += i * (N//i)
    print(ans)
