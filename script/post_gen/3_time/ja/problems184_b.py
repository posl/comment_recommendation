Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "o":
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)

main()

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'o':
            x += 1
        else:
            if x > 0:
                x -= 1
    print(x)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "o":
            X += 1
        else:
            X -= 1
            if X < 0:
                X = 0
    print(X)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "o":
            X += 1
        else:
            if X != 0:
                X -= 1
    print(X)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    s = input()
    for i in s:
        if i == 'o':
            x += 1
        else:
            if x > 0:
                x -= 1
    print(x)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    S = input()
    for i in S:
        if i == 'o':
            X += 1
        elif i == 'x':
            if X > 0:
                X -= 1
    print(X)

=======
Suggestion 8

def main():
    #入力
    N, X = map(int, input().split())
    S = input()
    #処理
    for i in range(N):
        if S[i] == "o":
            X += 1
        else:
            if X > 0:
                X -= 1
    #出力
    print(X)
