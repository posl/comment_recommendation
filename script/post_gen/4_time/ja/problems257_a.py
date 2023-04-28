Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n, x = map(int, input().split())
    print(chr(ord('A') + (x - 1) % 26) * n)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    print(chr(64 + (x - 1) % 26))

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    print(chr(x % 26 + 64))

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    print(chr(65 + (X - 1) % 26))

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    print(chr(64 + (X - 1) % 26))

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    print(chr(65 + ((X - 1) % 26)))

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    ans = ""
    for i in range(26):
        if n * (i + 1) >= x:
            ans = chr(65 + i)
            break
    print(ans)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    print(chr(64+n*(x-1)//26))

=======
Suggestion 9

def main():
    n,x=map(int,input().split())
    print(chr(ord("A")+(x-1)//n))
