Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:P-1] + A[Q:R-1] + A[S-1:]
    print(*B)

=======
Suggestion 2

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[P-1:Q] + A[R-1:S]
    print(*B)

=======
Suggestion 3

def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[:]
    b[p-1:q] = a[r-1:s]
    b[r-1:s] = a[p-1:q]
    print(*b)

=======
Suggestion 4

def solve():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:P-1] + A[Q:R-1] + A[S-1:] + A[R-1:Q] + A[P-1:R-1]
    print(*B)

=======
Suggestion 5

def main():
    #入力
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    #出力
    print(*A[:P-1], *A[Q:R-1], *A[S:], *A[R-1:Q], *A[P-1:R-1])

=======
Suggestion 6

def main():
    #入力
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    #出力
    print(*A[:P-1], *A[Q:R-1], *A[S-1:], *A[R-1:Q], *A[P-1:Q])

=======
Suggestion 7

def main():
    #入力
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    #入れ替え
    B = A[:P-1] + A[Q:R-1] + A[S:] + A[R-1:Q] + A[P-1:R-1]
    #出力
    print(*B)

=======
Suggestion 8

def main():
    #入力
    N,P,Q,R,S=map(int,input().split())
    A=list(map(int,input().split()))
    #処理
    B=A[:P-1]+A[Q:R-1]+A[S:]+A[P-1:Q]+A[R-1:S]
    #出力
    print(*B)

=======
Suggestion 9

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))

    #AのP番目からQ番目の項までとR番目からS番目の項までを入れ替えた数列をBとする
    B = A[:P-1] + A[R-1:S] + A[Q:S-1] + A[P-1:R-1] + A[S:]
    print(' '.join(map(str, B)))

=======
Suggestion 10

def main():
    #入力
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,P,Q,R,S)
    #print(A)
    #処理
    #数列 A の P 番目から Q 番目の項までと R 番目から S 番目の項までを入れ替えた数列を B=(B_1, B_2,..., B_N) とします。
    #数列 B を出力してください。
    #B = A[0:P-1] + A[Q:R-1] + A[S:N]
    B = A[0:P-1] + A[Q:R-1] + A[S:N]
    #出力
    print(B)
