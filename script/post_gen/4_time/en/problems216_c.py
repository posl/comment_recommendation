Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = ''
    while N > 0:
        if N % 2 == 0:
            S = 'B' + S
            N //= 2
        else:
            S = 'A' + S
            N -= 1
    print(S)

=======
Suggestion 2

def solve(n):
    s = ''
    while n > 0:
        if n % 2 == 0:
            s = 'B' + s
            n //= 2
        else:
            s = 'A' + s
            n -= 1
    return s

n = int(input())
print(solve(n))

=======
Suggestion 3

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 1:
            S = "A" + S
            N -= 1
        else:
            S = "B" + S
            N //= 2
    print(S)

=======
Suggestion 4

def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            s = "B" + s
            n = n // 2
        else:
            s = "A" + s
            n -= 1
    print(s)

=======
Suggestion 5

def main():
    N = int(input())
    S = ''
    while N > 0:
        if N % 2 == 0:
            S += 'B'
            N //= 2
        else:
            S += 'A'
            N -= 1
    print(S[::-1])

=======
Suggestion 6

def solve(n):
    s = ''
    while n > 0:
        if n % 2 == 0:
            n //= 2
            s = 'B' + s
        else:
            n -= 1
            s = 'A' + s
    return s

n = int(input())
print(solve(n))

=======
Suggestion 7

def main():
    N = int(input())
    ans = ''
    while N > 0:
        if N % 2 == 0:
            ans = 'B' + ans
            N //= 2
        else:
            ans = 'A' + ans
            N -= 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = ''
    while N > 0:
        if N % 2 == 0:
            ans = 'B' + ans
            N = N // 2
        else:
            ans = 'A' + ans
            N = N - 1
    print(ans)

=======
Suggestion 9

def solve(n):
    if n == 1:
        return "A"
    if n % 2 == 0:
        return solve(n//2) + "B"
    else:
        return solve(n-1) + "A"

=======
Suggestion 10

def main():
    N = int(input())
    s = ''
    while N > 0:
        if N % 2 == 0:
            s = 'B' + s
            N = N // 2
        else:
            s = 'A' + s
            N -= 1
    print(s)
