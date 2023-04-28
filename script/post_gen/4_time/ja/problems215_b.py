Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    k = 0
    while 2**k <= n:
        k += 1
    print(k-1)

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    k = 0
    while 2 ** k <= N:
        k += 1
    print(k - 1)

=======
Suggestion 4

def main():
    n = int(input())
    k = 0
    while True:
        if n < 2**k:
            break
        k += 1
    print(k-1)

=======
Suggestion 5

def main():
    N = int(input())
    for i in range(0, 60):
        if (2**i) > N:
            print(i-1)
            break

=======
Suggestion 6

def main():
    import sys
    import math
    n = int(input())
    print(math.floor(math.log2(n)))
    return

=======
Suggestion 7

def main():
    import sys
    import math

    n = int(input())
    print(math.floor(math.log2(n)))
