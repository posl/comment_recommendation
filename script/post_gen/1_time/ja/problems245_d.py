Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] // A[0]
    for i in range(M + 1):
        for j in range(N + 1):
            C[i + j] -= B[i] * A[j]
    print(' '.join(map(str, B)))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] // A[0]
        for j in range(N + 1):
            C[i + j] -= B[i] * A[j]
    print(*B)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [0] * (M + 1)
    B[0] = C[0] // A[0]
    for i in range(1, M + 1):
        B[i] = (C[i] - sum([A[j] * B[i - j] for j in range(1, i + 1)])) // A[0]
    print(*B)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for _ in range(M+1)]
    for i in range(M+1):
        B[i] = C[i+N] - sum([A[j] * B[i-j] for j in range(i)])
        B[i] //= A[0]
    print(*B)

=======
Suggestion 5

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    C=list(map(int,input().split()))
    B=[0]*(M+1)
    for i in range(M+1):
        B[i]=C[i+N]
        for j in range(N):
            B[i]-=A[j]*B[i-j-1]
        B[i]/=A[N]
    print(*B)

=======
Suggestion 6

def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #処理
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] // A[0]

    #出力
    print(*B)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    b = [0 for i in range(M+1)]
    for i in range(M+1):
        b[i] = c[i] // a[0]

    for i in range(M+1):
        for j in range(N+1):
            c[i+j] -= b[i] * a[j]

    print(" ".join(map(str, b)))

=======
Suggestion 8

def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    #出力
    B = []
    for i in range(M+1):
        B.append(C[i+N] - sum([A[j]*C[i+j] for j in range(N)]))
    print(*B)

=======
Suggestion 9

def main():
    # 入力受け取り
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # 逆順にしておく
    a.reverse()
    c.reverse()
    # 多項式の係数の積を計算
    b = [0] * (m + 1)
    for i in range(m + 1):
        b[i] = c[i] // a[0]
        for j in range(n + 1):
            c[i + j] -= b[i] * a[j]
    # 逆順に戻す
    b.reverse()
    # 結果出力
    print(' '.join(map(str, b)))
