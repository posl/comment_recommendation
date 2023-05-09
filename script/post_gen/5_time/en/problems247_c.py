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

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)

n = int(input())
print(*S(n))

=======
Suggestion 3

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

n = int(input())
print(' '.join(map(str, s(n))))

=======
Suggestion 4

def seq(n):
    if n == 1:
        return [1]
    else:
        s = seq(n-1)
        return s + [n] + s

n = int(input())
print(*seq(n))

=======
Suggestion 5

def main():
    n = int(input())
    s = [1]
    for i in range(1, n):
        s = s + [i + 1] + s
    print(*s)

=======
Suggestion 6

def main():
    n = int(input())
    s = [1]
    for i in range(1, n):
        s = s + [i + 1] + s
    print(*s, sep=' ')

=======
Suggestion 7

def main():
    N = int(input())
    S = [1]
    for i in range(1,N):
        S = S + [i+1] + S
    print(*S)

=======
Suggestion 8

def get_sequence(n):
    if n == 1:
        return [1]
    else:
        seq = get_sequence(n-1)
        return seq + [n] + seq

n = int(input())
for i in get_sequence(n):
    print(i, end=" ")

=======
Suggestion 9

def main():
    N = int(input())
    print(*sequence(N))
