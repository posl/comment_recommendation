Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

n = int(input())
print(*s(n))

=======
Suggestion 2

def f(n):
    if n == 1:
        return [1]
    else:
        return f(n-1) + [n] + f(n-1)

n = int(input())
print(*f(n))

=======
Suggestion 3

def main():
    n = int(input())
    s = [1]
    for i in range(1, n):
        s = s + [i + 1] + s
    print(*s)

=======
Suggestion 4

def main():
    n = int(input())
    s = "1"
    for i in range(1,n):
        s = s + str(i+1) + s
    print(s)

=======
Suggestion 5

def rec(n):
    if n == 1:
        return [1]
    else:
        return rec(n-1) + [n] + rec(n-1)

n = int(input())

print(*rec(n))

=======
Suggestion 6

def solve(n):
    if n == 1:
        return [1]
    else:
        return solve(n-1) + [n] + solve(n-1)

N = int(input())
print(*solve(N))

=======
Suggestion 7

def main():
    N = int(input())
    S = [1]
    for i in range(2,N+1):
        S = S + [i] + S
    print(*S)

=======
Suggestion 8

def print_seq(n):
    if n == 1:
        print(1, end=" ")
        return
    print_seq(n-1)
    print(n, end=" ")
    print_seq(n-1)

=======
Suggestion 9

def main():
    n = int(input())
    if n == 1:
        print(1)
        exit()
    else:
        s = [1]
        for i in range(2,n+1):
            s += [i] + s
        print(*s)
