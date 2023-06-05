Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n):
    if n == 1:
        return 'A'
    elif n % 2 == 0:
        return 'B' + solve(n // 2)
    else:
        return 'A' + solve(n - 1)

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    while n > 0:
        if n % 2 == 0:
            s.append('B')
            n = int(n/2)
        else:
            s.append('A')
            n -= 1
    s.reverse()
    print(''.join(s))

=======
Suggestion 3

def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            s = "B" + s
        else:
            n -= 1
            s = "A" + s
    print(s)

=======
Suggestion 4

def solve(n):
    s = ""
    while n > 0:
        if n % 2 == 0:
            s = "B" + s
            n = n // 2
        else:
            s = "A" + s
            n -= 1
    return s

=======
Suggestion 5

def main():
    N = int(input())
    S = ''
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            S = 'B' + S
        else:
            N -= 1
            S = 'A' + S
    print(S)

=======
Suggestion 6

def solve(n):
    ans = ''
    while n > 0:
        if n % 2 == 0:
            n //= 2
            ans += 'B'
        else:
            n -= 1
            ans += 'A'
    return ans[::-1]

=======
Suggestion 7

def solve(n):
    s = ""
    while n > 0:
        if n % 2 == 0:
            n //= 2
            s += "B"
        else:
            n -= 1
            s += "A"
    return s[::-1]

n = int(input())
print(solve(n))

=======
Suggestion 8

def solve(n):
    if n == 1:
        return 'A'
    elif n == 2:
        return 'B'
    elif n % 2 == 0:
        return solve(n // 2) + 'B'
    else:
        return solve(n - 1) + 'A'

=======
Suggestion 9

def main():
    N = int(input())
    n = N
    ans = ''
    while n > 0:
        if n % 2 == 1:
            ans = 'A' + ans
            n -= 1
        else:
            ans = 'B' + ans
            n //= 2
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    s = ''
    while n > 0:
        if n % 2 == 0:
            s += 'B'
            n = n // 2
        else:
            s += 'A'
            n -= 1
    print(s[::-1])
