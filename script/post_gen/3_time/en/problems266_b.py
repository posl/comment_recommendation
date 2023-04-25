Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N > 0:
        print(N % 998244353)
    elif N < 0:
        print(998244353 + (N % 998244353))
    else:
        print(0)

=======
Suggestion 2

def main():
    N = int(input())
    if N > 0:
        print(N % 998244353)
    else:
        print(998244353 - (abs(N) % 998244353))

=======
Suggestion 3

def main():
    N = int(input())
    print((N + 998244353) % 998244353)

=======
Suggestion 4

def main():
    N = int(input())
    print(N%998244353)

=======
Suggestion 5

def main():
    N = int(input())
    print((N%998244353-998244353)%998244353)

=======
Suggestion 6

def main():
    N = int(input())
    x = (N % 998244353)
    print(x)

=======
Suggestion 7

def main():
    n = int(input())
    print(-n % 998244353)

=======
Suggestion 8

def main():
    n = int(input())
    print((n-1)%998244353)
