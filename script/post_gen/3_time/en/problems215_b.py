Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    k = 0
    while 2**k <= N:
        k += 1
    print(k-1)

main()

=======
Suggestion 2

def main():
    N = int(input())
    k = 0
    while 2**k <= N:
        k += 1
    print(k-1)

=======
Suggestion 3

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
Suggestion 4

def main():
    N = int(input())

    i = 0
    while 2**i <= N:
        i += 1

    print(i-1)

=======
Suggestion 5

def main():
    N = int(input())
    for k in reversed(range(61)):
        if 2**k <= N:
            print(k)
            break

=======
Suggestion 6

def main():
    N = int(input())
    print(N.bit_length()-1)
