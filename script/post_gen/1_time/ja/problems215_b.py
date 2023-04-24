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
    print(N.bit_length()-1)

=======
Suggestion 3

def main():
    n = int(input())
    print(n.bit_length() - 1)
