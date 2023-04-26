Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    print(chr(ord('A') + (x - 1) % 26) * n)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    print(chr(65 + (x - 1) % 26) * n)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    print(chr(x % 26 + 64))

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    print(chr(ord('A') + x//n - 1))

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    print(chr(X % 26 + 64))

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    print(chr(64+x//n))

=======
Suggestion 7

def main():
    N,X = map(int,input().split())
    #print(N,X)
    for i in range(1,N+1):
        if X <= 26*i:
            print(chr(65+N-i))
            break
        else:
            X -= 26*i
    return
