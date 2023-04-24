Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N % 998244353 == 0:
        print(0)
    else:
        print(998244353 - N % 998244353)

=======
Suggestion 2

def main():
    N = int(input())
    if N % 998244353 == 0:
        print(0)
    else:
        print(998244353 - (N % 998244353))

=======
Suggestion 3

def main():
    N = int(input())
    print(N%998244353)

=======
Suggestion 4

def main():
    N = int(input())
    print((N + 998244353) % 998244353)

=======
Suggestion 5

def main():
    N = int(input())
    print((N%998244353-998244353)%998244353)

=======
Suggestion 6

def main():
    N = int(input())
    print((-N) % 998244353)

=======
Suggestion 7

def main():
    n = int(input())
    print((n+998244353)%998244353)
