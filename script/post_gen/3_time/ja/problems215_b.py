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
    N = int(input())
    if N == 1:
        print(0)
    else:
        k = 0
        while 2**k <= N:
            k += 1
        print(k-1)

=======
Suggestion 3

def main():
    N = int(input())
    k = 0
    while (2**k) <= N:
        k += 1
    print(k-1)

=======
Suggestion 4

def main():
    N = int(input())
    print(N.bit_length()-1)

main()
