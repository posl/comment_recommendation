Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    print(chr(ord('A') + x//n - 1))

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    print(chr(x - 1 + ord('A')))

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    print(chr(X - 1 + ord('A')))

=======
Suggestion 4

def get_char(n, x):
    n = int(n)
    x = int(x)
    if x <= n:
        return chr(ord('A') + x - 1)
    else:
        return get_char(n, x - n) 

n, x = input().split()
print(get_char(n, x))

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    print(chr(64 + (X-1) % 26))

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    print(chr(64+X//N))

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    print(chr(x + 64))

main()

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(alpha[x % 26 - 1])

=======
Suggestion 9

def readinput():
    n,x=list(map(int,input().split()))
    return n,x

=======
Suggestion 10

def getNthCharOfConcatenatedString(N, X):
    return chr(ord('A') + (X - 1) % 26)
