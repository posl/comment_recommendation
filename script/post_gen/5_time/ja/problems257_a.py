Synthesizing 10/10 solutions

=======
Suggestion 1

def get_char(n, x):
    # n: 何文字目までの文字列を作るか
    # x: 何文字目の文字を取得するか
    # 1

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    print(chr(x%26+64))

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    print(chr(65 + (x - 1) % 26) * n)

=======
Suggestion 4

def main():
    n,x = map(int,input().split())
    print(chr(ord('A') + (x-1) % 26) * n)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    ans = ""
    for i in range(n):
        ans += chr(65 + i) * n
    print(ans[x - 1])

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    print(chr(x + 64))

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    print(chr(64 + X // N))

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    print(chr(ord('A') + (x-1)%26))

=======
Suggestion 9

def main():
    n,x = map(int,input().split())
    print(chr(64+x//n))

=======
Suggestion 10

def main():
    n,x = map(int,input().split())
    ans = ''
    for i in range(n):
        ans += chr(i+65)*n
    print(ans[x-1])
