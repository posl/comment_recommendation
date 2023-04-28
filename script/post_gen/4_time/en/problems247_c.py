Synthesizing 10/10 solutions

=======
Suggestion 1

def S(n):
    if n == 1:
        return "1"
    else:
        return S(n-1) + " " + str(n) + " " + S(n-1)

print(S(int(input())))

=======
Suggestion 2

def sequence(n):
    if n == 1:
        return [1]
    else:
        return sequence(n-1) + [n] + sequence(n-1)

=======
Suggestion 3

def seq(n):
    if n == 1:
        return [1]
    else:
        return seq(n-1) + [n] + seq(n-1)

n = int(input())
print(' '.join(map(str, seq(n))))

=======
Suggestion 4

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n - 1) + [n] + S(n - 1)

n = int(input())
print(*S(n))

=======
Suggestion 5

def S(n):
    if n == 1:
        return [1]
    else:
        s = S(n-1)
        return s + [n] + s

N = int(input())
print(*S(N))

=======
Suggestion 6

def main():
    n = int(input())
    s = [1]
    for i in range(1, n):
        s = s + [i + 1] + s
    print(" ".join(map(str, s)))

=======
Suggestion 7

def main():
    n = int(input())
    ans = [1]
    for i in range(2, n+1):
        ans = ans + [i] + ans
    print(*ans)

=======
Suggestion 8

def main():
    n = int(input())
    seq = [1]
    for i in range(1, n):
        seq = seq + [i + 1] + seq

    print(" ".join(str(x) for x in seq))

=======
Suggestion 9

def generate_sequence(n):
    if n == 1:
        return [1]
    else:
        sequence = generate_sequence(n-1)
        return sequence + [n] + sequence

=======
Suggestion 10

def solution():
    N = int(input())
    S = [1]
    for i in range(1, N):
        S = S + [i+1] + S
    print(*S)

solution()
