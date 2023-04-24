Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    x = 998244353 - abs(n) % 998244353
    if n < 0:
        x = 998244353 - x
    print(x)

=======
Suggestion 2

def main():
    N = int(input())
    print((N + 998244353) % 998244353)

=======
Suggestion 3

def main():
    N = int(input())
    print(N%998244353)

=======
Suggestion 4

def main():
    N = int(input())
    print((-N)%998244353)

=======
Suggestion 5

def main():
    n = int(input())
    print((n+998244353) % 998244353)

main()

=======
Suggestion 6

def main():
    N = int(input())
    print((N%998244353))

=======
Suggestion 7

def main():
    N = int(input())
    x = (N%998244353)
    print(x)

=======
Suggestion 8

def main():
    N = int(input())
    print((N%998244353)*(-1))
