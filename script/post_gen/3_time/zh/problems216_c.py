Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = ''
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            ans += 'B'
        else:
            n -= 1
            ans += 'A'
    print(ans[::-1])

=======
Suggestion 2

def solve(num):
    res = []
    while num > 0:
        if num % 2 == 0:
            num = num // 2
            res.append('B')
        else:
            num -= 1
            res.append('A')
    res.reverse()
    return ''.join(res)

print(solve(int(input())))

=======
Suggestion 3

def solve(n):
    if n == 1:
        return 'A'
    if n % 2 == 0:
        return solve(n // 2) + 'B'
    else:
        return solve(n - 1) + 'A'

=======
Suggestion 4

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
Suggestion 5

def f(n):
    if n == 0:
        return ''
    if n == 1:
        return 'A'
    if n % 2 == 0:
        return f(n // 2) + 'B'
    else:
        return f(n - 1) + 'A'

n = int(input())
print(f(n))

=======
Suggestion 6

def solve(n):
    ans = ""
    while n > 0:
        if n % 2 == 0:
            n //= 2
            ans += "B"
        else:
            n -= 1
            ans += "A"
    return ans[::-1]

=======
Suggestion 7

def main():
    n = int(input())
    s = ''
    while n>0:
        if n%2 == 0:
            s = 'B' + s
            n = n//2
        else:
            s = 'A' + s
            n -= 1
    print(s)

=======
Suggestion 8

def solve(n):
    if n == 1:
        return 'A'
    if n % 2 == 0:
        return solve(n // 2) + 'B'
    else:
        return solve(n - 1) + 'A'

print(solve(int(input())))

=======
Suggestion 9

def solve(n):
    s = ''
    while n != 0:
        if n % 2 == 1:
            s = 'A' + s
            n -= 1
        else:
            s = 'B' + s
            n //= 2
    return s

=======
Suggestion 10

def solve(n):
    if n == 1:
        return 'A'
    if n % 2 == 0:
        return solve(n // 2) + 'B'
    else:
        return solve(n - 1) + 'A'

n = int(input())
print(solve(n))
