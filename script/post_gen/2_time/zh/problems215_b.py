Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    k = 0
    while True:
        if 2**k <= N:
            k += 1
        else:
            break
    print(k-1)

=======
Suggestion 2

def main():
    n = int(input())
    k = 0
    while 2 ** k <= n:
        k += 1
    print(k - 1)

=======
Suggestion 3

def main():
    N = int(input())
    k = 0
    while N > 1:
        N /= 2
        k += 1
    print(k)

=======
Suggestion 4

def main():
    N = int(input())
    k = 0
    while 2**k <= N:
        k += 1
    print(k-1)

=======
Suggestion 5

def main():
    n = int(input())
    k = 0
    while 1<<k <= n:
        k += 1
    print(k-1)

=======
Suggestion 6

def calc_max_k(N):
    k = 0
    while True:
        if 2 ** k <= N:
            k += 1
        else:
            break
    return k - 1

=======
Suggestion 7

def get_k(n):
    k = 0
    while True:
        if 2**k <= n < 2**(k+1):
            break
        k += 1
    return k

=======
Suggestion 8

def main():
    N = int(input())
    k = 0
    while True:
        if 2**k > N:
            break
        k += 1
    print(k-1)
