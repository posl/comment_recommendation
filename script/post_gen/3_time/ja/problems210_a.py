Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(N * X)
    else:
        print(A * X + (N - A) * Y)

=======
Suggestion 2

def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(X * N)
    else:
        print(X * A + Y * (N - A))

=======
Suggestion 3

def main():
    N, A, X, Y = map(int, input().split())
    if N > A:
        print((N - A) * Y + A * X)
    else:
        print(N * X)

=======
Suggestion 4

def main():
    #入力
    N,A,X,Y = map(int,input().split())

    #処理
    if N <= A:
        ans = X * N
    else:
        ans = X * A + Y * (N - A)
    
    #出力
    print(ans)
