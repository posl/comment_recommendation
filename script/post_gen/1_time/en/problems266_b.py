Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N >= 0:
        print(N % 998244353)
    else:
        print(998244353 - (-N % 998244353))

=======
Suggestion 2

def main():
    N = int(input())
    print((N - N // 998244353 * 998244353) % 998244353)

=======
Suggestion 3

def main():
    n = int(input())
    print((n + 998244353) % 998244353)

=======
Suggestion 4

def main():
    N = int(input())
    print(N%998244353)

=======
Suggestion 5

def main():
    N = int(input())
    print(998244353 - (N % 998244353))

=======
Suggestion 6

def main():
    N = int(input())
    print((N % 998244353) * -1)

=======
Suggestion 7

def main():
    n = int(input())
    print(n%998244353)

=======
Suggestion 8

def main():
    N = int(input())
    print((N%998244353-998244353)*-1)

=======
Suggestion 9

def main():
    N = int(input())
    print((N%998244353))

=======
Suggestion 10

def solve(n):
    return (n - 1) % 998244353
