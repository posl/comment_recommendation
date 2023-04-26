Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * n
    for i in range(n-1):
        cnt[a[i]-1] += 1
    for i in range(n):
        print(cnt[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0 for _ in range(N)]
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])
    return

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    subordinates = [0] * N
    for a in A:
        subordinates[a-1] += 1
    for s in subordinates:
        print(s)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    C = [0] * N
    for i in range(N-1):
        C[A[i]-1] += 1
    for c in C:
        print(c)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #部下の数を数える
    sub = [0] * N
    for i in range(N - 1):
        sub[A[i] - 1] += 1
    #部下の数を出力
    for i in range(N):
        print(sub[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #上司の人数を数える
    boss = [0] * (N+1)
    for i in range(N-1):
        boss[A[i]] += 1

    #下の人数を数える
    subordinate = [0] * (N+1)
    for i in range(N-1):
        subordinate[i+2] = boss[i+2]
        subordinate[i+2] += subordinate[A[i]]

    print(*subordinate[1:], sep='

')

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #社員数分のリストを作成
    ans = [0] * N
    #社員番号1の社員以外について
    for i in range(1, N):
        #直属の上司に1人追加
        ans[A[i] - 1] += 1
    #出力
    for i in range(N):
        print(ans[i])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 部下の数をカウントする配列
    # 0番目は使わない
    cnt = [0] * (N + 1)

    # 部下の数をカウント
    for i in range(N - 1):
        cnt[A[i]] += 1

    # 部下の数を出力
    for i in range(1, N + 1):
        print(cnt[i])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A[i] = i+1 の上司の番号
    # A[i] = i+1 の部下の数
    # A[i] = 1 の部下の数
    for i in range(N-1, 0, -1):
        A[A[i]-1] += A[i]
    for i in range(N):
        print(A[i])
