Synthesizing 10/10 solutions

=======
Suggestion 1

def problems266_b():
    N = int(input())
    print((998244353-N%998244353)%998244353)

=======
Suggestion 2

def main():
    N = int(input())
    print((N % 998244353 + 998244353) % 998244353)

=======
Suggestion 3

def main():
    N = int(input())
    print((998244353 - N % 998244353) % 998244353)

=======
Suggestion 4

def main():
    n = int(input())
    print(n%998244353)

=======
Suggestion 5

def main():
    n = int(input())
    print(998244353 - n % 998244353)
main()

=======
Suggestion 6

def main():
    n = int(input())
    print((n % 998244353 + 998244353) % 998244353)

=======
Suggestion 7

def solve(n):
    return n % 998244353

=======
Suggestion 8

def main():
    N = int(input())
    print(N%998244353)

=======
Suggestion 9

def solve(n):
    if n < 0:
        n = -n
        n = n % 998244353
        n = 998244353 - n
    else:
        n = n % 998244353
    return n

=======
Suggestion 10

def solve(n):
    return (998244353 - n % 998244353) % 998244353
