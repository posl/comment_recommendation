Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N - 1):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N - 1):
        B[A[i] - 1] += 1
    print(*B, sep = '

')

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N-1):
        B[A[i]-1] += 1
    for b in B:
        print(b)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = [0] * N
    for i in range(N-1):
        C[A[i]-1] += 1
    for c in C:
        print(c)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    for i in range(N - 1):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * n
    for i in range(n - 1):
        cnt[a[i + 1] - 1] += 1
    for i in range(n):
        print(cnt[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    B = [0]*N
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 直属の部下を数える
    subordinates = [0] * n
    for i in range(n - 1):
        subordinates[a[i] - 1] += 1

    # 結果を出力
    for i in range(n):
        print(subordinates[i])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 1から始まるので、要素数はn+1にする
    # このリストのi番目は、社員番号iの部下の数
    b = [0] * (n+1)

    # aの要素を走査する
    for i in a:
        # aの要素は、社員番号iの直属の上司
        # したがって、社員番号iの部下の数を1増やす
        b[i] += 1

    # 1からnまでの社員の部下の数を出力する
    for i in range(1, n+1):
        print(b[i])
