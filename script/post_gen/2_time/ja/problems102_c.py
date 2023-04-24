Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - (i + 1) for i in range(N)]
    A.sort()
    b = A[N // 2]
    print(sum([abs(a - b) for a in A]))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (i+1))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - i - 1 for i in range(N)]
    A.sort()
    b = A[N//2]
    print(sum(abs(b - a) for a in A))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N):
        ans = min(ans, abs(A[i] - (i + 1)))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 10**10
    for i in range(N):
        ans = min(ans, abs(A[i] - (i+1)))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = float('inf')
    for i in range(1,N+1):
        ans = min(ans,abs(A[i-1]-i))
    print(ans)

=======
Suggestion 7

def main():
    # 入力
    N = int(input())
    A = list(map(int, input().split()))
    # 処理
    A = [a - (i + 1) for i, a in enumerate(A)]
    A.sort()
    b = A[N // 2]
    print(sum([abs(a - b) for a in A]))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 10**9
    for i in range(n):
        tmp = a[i] - (i+1)
        ans = min(ans, tmp)
    ans = abs(ans)
    sum = 0
    for i in range(n):
        sum += abs(a[i] - (i+1) - ans)
    print(sum)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # b = 0 とする
    b = 0
    # すぬけ君の悲しさの値を計算
    sadness = 0
    for i in range(N):
        sadness += abs(A[i] - (b + i + 1))

    # b = 1 ~ N として、すぬけ君の悲しさの値を計算し、最小値を求める
    for i in range(1, N):
        # すぬけ君の悲しさの値を計算
        sadness_tmp = 0
        for j in range(N):
            sadness_tmp += abs(A[j] - (i + j + 1))

        # すぬけ君の悲しさの値が最小値なら更新
        if sadness_tmp < sadness:
            sadness = sadness_tmp

    print(sadness)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # b = 0 の時の悲しさ
    b = 0
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b + i + 1))

    # b = 1 の時の悲しさ
    b = 1
    tmp = 0
    for i in range(n):
        tmp += abs(a[i] - (b + i + 1))

    # b = 1 の時の悲しさが最小の場合
    if tmp < ans:
        ans = tmp

    # b = -1 の時の悲しさ
    b = -1
    tmp = 0
    for i in range(n):
        tmp += abs(a[i] - (b + i + 1))

    # b = -1 の時の悲しさが最小の場合
    if tmp < ans:
        ans = tmp

    print(ans)
