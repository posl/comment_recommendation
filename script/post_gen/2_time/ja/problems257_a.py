Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    print(chr(ord('A') + (x - 1) // n))

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    for i in range(N):
        ans += alphabet[(X - 1) % 26]
        X = (X - 1) // 26
    print(ans[::-1])

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    for i in range(N):
        ans += S[(X-1)%26]
        X = (X-1)//26
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    S = ''
    for i in range(1, N + 1):
        for j in range(65, 91):
            S += chr(j)
    print(S[X - 1])

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    ans = ""
    for i in range(1, N + 1):
        ans += chr(65 + (X - i) // N)
    print(ans)

main()

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    print(chr(X // N + 64 + X % N))

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(alphabet[(X-1) % 26])

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(s[(x-1)%n])

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    A = ord("A")
    print(chr(A + (X-1) % N))

=======
Suggestion 10

def main():
    n,x = map(int,input().split())
    print(chr(64+n+(x-n)%26))
