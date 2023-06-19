Synthesizing 10/10 solutions

=======
Suggestion 1

def getChar(n,x):
    return chr(ord('A')+x//n)

=======
Suggestion 2

def main():
    N,X = map(int,input().split())
    if X%N == 0:
        print(chr(64+N))
    else:
        print(chr(64+X%N))

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    list1 = []
    for i in range(n):
        for j in range(65,91):
            list1.append(chr(j))
    print(list1[x-1])

=======
Suggestion 4

def problem257_a(n, x):
    for i in range(1, 27):
        if x <= i * n:
            return chr(65 + i - 1)

=======
Suggestion 5

def problem257_a():
    n, x = [int(i) for i in input().split()]
    print(chr(ord('A') + x // n - 1), end='')

=======
Suggestion 6

def get_char(n, x):
    if n == 1:
        return chr(x + 64)
    elif x <= n:
        return chr(x + 64)
    else:
        return chr(x % n + 64)

=======
Suggestion 7

def main():
    n, x = map(int, raw_input().split())
    if x % n == 0:
        print chr((x / n) + 64)
    else:
        print chr((x / n) + 65)

=======
Suggestion 8

def problem257_a(n, x):
    return chr((x - 1) % 26 + ord('A'))

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    print(chr(X%N+64))

=======
Suggestion 10

def problems257_a():
    n, x = map(int, raw_input().split())
    print chr(64 + (x-1)/n)
