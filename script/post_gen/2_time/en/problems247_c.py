Synthesizing 10/10 solutions

=======
Suggestion 1

def sequence(n):
    if n == 1:
        return "1"
    else:
        return sequence(n-1) + " " + str(n) + " " + sequence(n-1)

=======
Suggestion 2

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)
n = int(input())
print(*s(n))

=======
Suggestion 3

def seq(n):
    if n == 1:
        return [1]
    else:
        return seq(n-1) + [n] + seq(n-1)

N = int(input())
print(' '.join(map(str, seq(N))))

=======
Suggestion 4

def seq(n):
    if n == 1:
        return [1]
    else:
        return seq(n-1) + [n] + seq(n-1)

n = int(input())
print(' '.join(map(str,seq(n))))

=======
Suggestion 5

def main():
    n = int(input())
    s = [1]
    for i in range(1, n):
        s = s + [i+1] + s
    print(' '.join(map(str, s)))

=======
Suggestion 6

def main():
    n = int(input())
    print('1', end=' ')
    for i in range(2, n+1):
        print(i, end=' ')
        print('1', end=' ')
        for j in range(2, i+1):
            print(j, end=' ')
            print('1', end=' ')
    print('')

=======
Suggestion 7

def sequence(n):
    if n == 1:
        return '1'
    else:
        return sequence(n-1) + str(n) + sequence(n-1)

print(sequence(int(input())))

=======
Suggestion 8

def main():
    n = int(input())
    s = [1]
    for i in range(1,n):
        s = s + [i+1] + s
    print(*s)

=======
Suggestion 9

def main():
    N = int(input())
    if N == 1:
        print("1")
        return
    S = [1]
    for i in range(2,N+1):
        S = S + [i] + S
    print(" ".join(map(str, S)))

=======
Suggestion 10

def main():
    n = int(input().strip())
    print(' '.join(map(str, get_seq(n))))
