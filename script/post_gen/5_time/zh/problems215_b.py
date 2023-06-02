Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    import math
    n = int(input())
    k = math.floor(math.log(n,2))
    print(k)

=======
Suggestion 2

def main():
    n = int(input())
    k = 0
    while True:
        if 2**k <= n:
            k += 1
        else:
            break
    print(k - 1)

=======
Suggestion 3

def main():
    n = int(input())
    k = 0
    while 2**k <= n:
        k += 1
    print(k-1)

=======
Suggestion 4

def main():
    N = int(input())
    k = 0
    while N >= 2:
        N /= 2
        k += 1
    print(k)

=======
Suggestion 5

def main():
    N = int(input())
    k = 0
    while 2**k <= N:
        k += 1
    print(k-1)

=======
Suggestion 6

def main():
    N = int(input())
    k = 0
    while N >= 2:
        N = N/2
        k = k + 1
    print(k)

=======
Suggestion 7

def main():
    n = int(input())
    k = 0
    while 2**k <= n:
        k = k + 1
    print(k-1)
main()
