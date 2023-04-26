Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = ''
    while n > 0:
        if n % 2 == 0:
            n //= 2
            ans += 'B'
        else:
            n -= 1
            ans += 'A'
    print(ans[::-1])

=======
Suggestion 2

def main():
    N = int(input())
    ans = []
    while N > 0:
        if N % 2 == 0:
            N //= 2
            ans.append("B")
        else:
            N -= 1
            ans.append("A")
    ans.reverse()
    print("".join(ans))

=======
Suggestion 3

def main():
    n = int(input())
    ans = []
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            ans.append('B')
        else:
            n -= 1
            ans.append('A')
    ans.reverse()
    print(''.join(ans))

=======
Suggestion 4

def solve():
    N = int(input())
    ans = ''
    while N > 0:
        if N % 2 == 0:
            ans += 'B'
            N //= 2
        else:
            ans += 'A'
            N -= 1
    print(ans[::-1])

=======
Suggestion 5

def solve(n):
    ans = []
    while n > 0:
        if n % 2 == 0:
            ans.append('B')
            n = n // 2
        else:
            ans.append('A')
            n -= 1
    return ''.join(ans[::-1])
n = int(input())
print(solve(n))

=======
Suggestion 6

def solve():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            S = "B" + S
            N //= 2
        else:
            S = "A" + S
            N -= 1
    print(S)
    return 0

=======
Suggestion 7

def solve(n):
    if n == 0:
        return ''
    if n % 2 == 0:
        return solve(n // 2) + 'B'
    else:
        return solve(n - 1) + 'A'

=======
Suggestion 8

def solve():
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
Suggestion 9

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N%2 == 0:
            S = "B" + S
            N = N//2
        else:
            S = "A" + S
            N = N-1
    print(S)

=======
Suggestion 10

def solve(N):
    res = []
    while N > 0:
        if N % 2 == 1:
            res.append('A')
            N -= 1
        else:
            res.append('B')
            N //= 2
    res.reverse()
    return "".join(res)
