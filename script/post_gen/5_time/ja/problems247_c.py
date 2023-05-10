Synthesizing 10/10 solutions

=======
Suggestion 1

def makeS(n):
    if n == 1:
        return [1]
    else:
        return makeS(n-1) + [n] + makeS(n-1)

N = int(input())
print(*makeS(N))

=======
Suggestion 2

def main():
    n = int(input())
    s = [1]
    for i in range(1,n):
        s = s + [i+1] + s
    print(*s)

=======
Suggestion 3

def make_s(n):
    if n == 1:
        return [1]
    else:
        s = make_s(n-1)
        return s + [n] + s

N = int(input())
print(*make_s(N))

=======
Suggestion 4

def main():
    N = int(input())
    S = [1]
    for i in range(1, N):
        S = S + [i + 1] + S
    print(' '.join(map(str, S)))

=======
Suggestion 5

def solve():
    n = int(input())
    ans = [1]
    for i in range(2,n+1):
        ans = ans + [i] + ans
    print(*ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = [1]
    for i in range(2, n + 1):
        s = s + [i] + s
    print(*s)

=======
Suggestion 7

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n - 1) + [n] + s(n - 1)
n = int(input())
print(*s(n))

=======
Suggestion 8

def makeS(n):
    if n == 1:
        return [1]
    else:
        return makeS(n-1) + [n] + makeS(n-1)

N = int(input())
S = makeS(N)
print(*S)

=======
Suggestion 9

def s(n):
    if n == 1:
        return [1]
    else:
        a = s(n - 1)
        return a + [n] + a

n = int(input())
print(*s(n))

=======
Suggestion 10

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

N = int(input())
print(*s(N))
