Synthesizing 10/10 solutions

=======
Suggestion 1

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

print(s(4))

=======
Suggestion 2

def sequence(n):
    if n == 1:
        return [1]
    else:
        s = sequence(n-1)
        return s + [n] + s

=======
Suggestion 3

def f(n):
    if n == 1:
        return [1]
    else:
        s = f(n-1)
        return s + [n] + s

n = int(input())
print(*f(n))

=======
Suggestion 4

def seq(n):
    if n == 1:
        return [1]
    else:
        s = seq(n-1)
        return s + [n] + s

=======
Suggestion 5

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

n = int(input())
print(*s(n))

=======
Suggestion 6

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)

N = int(input())
print(' '.join(map(str, S(N))))

=======
Suggestion 7

def S(n):
    if n==1:
        return [1]
    else:
        s = S(n-1)
        return s+[n]+s

N = int(input())
print(*S(N))

=======
Suggestion 8

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1)+[n]+s(n-1)

=======
Suggestion 9

def main():
    n = int(input())
    s = [1]
    for i in range(1,n):
        s = s + [i+1] + s
    print(*s)

=======
Suggestion 10

def f(n):
    if n == 1:
        return [1]
    else:
        a = f(n-1)
        return a + [n] + a

n = int(input())
print(*f(n))
