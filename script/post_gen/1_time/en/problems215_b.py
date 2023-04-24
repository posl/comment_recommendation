Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    k = 0
    while 2**k <= N:
        k += 1
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
    while (2**k <= N):
        k += 1
    print(k-1)

=======
Suggestion 4

def main():
    N = int(input())
    k = 0
    while N > 1:
        N >>= 1
        k += 1
    print(k)

main()

=======
Suggestion 5

def main():
    N = int(input())
    print(N.bit_length() - 1)
