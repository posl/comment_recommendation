Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i], end=" ")

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a for a in A if a != X]
    print(*A)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i for i in A if i != X]
    print(*A)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] == X:
            A[i] = 0
    for i in range(N):
        if A[i] != 0:
            print(A[i], end=" ")

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a for a in A if a != X]
    print(*A, sep=" ")

=======
Suggestion 6

def main():
    #入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #出力
    for i in range(N):
        if A[i] != X:
            print(A[i], end=" ")

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=" ")
        else:
            pass

=======
Suggestion 8

def main():
    #入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #処理
    #AからXと等しい要素を全て取り除き、残った要素をそのままの順序で並べた数列 A' を出力してください。
    #A'の要素を空白区切りで順に出力せよ。
    #A' が要素数 0 の数列となる場合があります。この場合、空行を出力するだけで構いません。
    A = [a for a in A if a != X]
    print(*A)
