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
    while 2**k <= N:
        k += 1
    print(k-1)

=======
Suggestion 3

def main():
    import sys
    n = int(sys.stdin.readline().strip())
    print((n-1).bit_length())
main()

=======
Suggestion 4

def main():
    import sys
    n = int(sys.stdin.readline().strip())
    k = 0
    while True:
        if 2 ** k > n:
            break
        k += 1
    print(k - 1)

=======
Suggestion 5

def main():
    n = int(input())
    print(int(math.log2(n)))

=======
Suggestion 6

def main():
    n = int(input())
    k = 0
    res = 1
    while True:
        if res > n:
            break
        res *= 2
        k += 1
    print(k-1)

=======
Suggestion 7

def solve():
    n = int(input())
    print(len(bin(n))-3)
solve()
