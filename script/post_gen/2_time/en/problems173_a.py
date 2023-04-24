Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print(1000 - N % 1000 if N % 1000 != 0 else 0)

main()

=======
Suggestion 2

def main():
    N = int(input())
    print(1000 - (N % 1000) if N % 1000 != 0 else 0)

=======
Suggestion 3

def main():
    n = int(input())
    print(n%1000)
    if n%1000 == 0:
        print(0)
    else:
        print(1000-(n%1000))

main()

=======
Suggestion 4

def main():
    N = int(input())
    print(N%1000)
    if N%1000 != 0:
        print(1000 - N%1000)
    else:
        print(0)

=======
Suggestion 5

def main():
    N = int(input())
    print(N % 1000 if N % 1000 != 0 else 1000)

=======
Suggestion 6

def main():
    # input
    N = int(input())

    # compute
    ans = N % 1000
    if ans != 0:
        ans = 1000 - ans

    # output
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    print(1000 - (N % 1000))

=======
Suggestion 8

def main():
    n = int(input())
    print(1000 - (n % 1000))
    return

=======
Suggestion 9

def main():
    N = int(input()) # N is an integer.
    print(1000 - (N % 1000) if N % 1000 != 0 else 0)
