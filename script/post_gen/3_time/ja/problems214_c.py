Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input()) # 1 <= N <= 200000
    S = list(map(int, input().split())) # 1 <= S_i <= 10^9
    T = list(map(int, input().split())) # 1 <= T_i <= 10^9
    #print(N, S, T)
    #print(S[0], S[1], S[2], S[3])
    #print(T[0], T[1], T[2], T[3])

    # 1 <= i <= N
    # i番目のすぬけくんが初めて宝石をもらう時刻を求める
    # すぬけくんが宝石をもらうとS_i単位時間後に、その宝石を(i+1)番目のすぬけくんに渡す
    # ただし、(N+1)番目のすぬけくんとは1番目のすぬけくんのことを指す
    # 高橋くんは時刻T_iにi番目のすぬけくんに宝石を渡す
    # すぬけくんの宝石の受け渡しにかかる時間は無視できる

    # 1 <= i <= N
    # i番目のすぬけくんが初めて宝石をもらう時刻を求める
    # すぬけくんが宝石をもらうとS_i単位時間後に、その宝石を(i+1)番目のすぬけくんに渡す
    # ただし、(N+1)番目のすぬけくんとは1番目のすぬけくんのことを指す
    # 高橋くんは時刻T_iにi番目のすぬけくんに宝石を渡す
    # すぬけくんの宝石の受け

=======
Suggestion 2

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    for i in range(n):
        ans = t[i]
        for j in range(n):
            if t[(i+j)%n] < ans:
                break
            ans = t[(i+j)%n] + s[(i+j)%n]
        print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = []
    for i in range(N):
        ans.append(T[i])
        for j in range(i+1, i+N):
            if ans[i] > T[j%N]:
                ans[i] = T[j%N]
            else:
                ans[i] += S[j%N]
    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    for i in range(N):
        print(T[i] - S[i])

=======
Suggestion 5

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    T = [(T[i], i + 1) for i in range(N)]
    T.sort()
    T = [0] + [T[i][1] for i in range(N)]
    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        if ans[i] == 0:
            ans[i] = T[i]
            j = T[i]
            while ans[j] == 0:
                ans[j] = T[i]
                j = T[j]
    for i in range(1, N + 1):
        print(ans[i])

=======
Suggestion 6

def main():
    import sys
    readline = sys.stdin.readline
    N = int(readline())
    S = list(map(int, readline().split()))
    T = list(map(int, readline().split()))

    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(N):
        if ans[i] > ans[(i+1)%N]:
            ans[(i+1)%N] = ans[i] + S[i]
    for i in range(N-1, -1, -1):
        if ans[i] > ans[(i+1)%N]:
            ans[(i+1)%N] = ans[i] + S[i]
    for i in range(N):
        print(ans[i])

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    # すぬけくんが宝石を受け取る時刻のリスト
    A = [0] * N
    # 高橋くんが宝石を渡す時刻のリスト
    B = [0] * N
    # 高橋くんが渡した宝石の受け取り時刻のリスト
    C = [0] * N
    # すぬけくんが宝石を受け取る時刻を計算
    for i in range(N):
        A[i] = T[i] + S[i]
    # 高橋くんが渡した宝石の受け取り時刻を計算
    for i in range(N):
        B[i] = A[i] + S[(i+1) % N]
    # すぬけくんが宝石を受け取る時刻を計算
    for i in range(N):
        C[i] = B[i] + S[(i+2) % N]
    # すぬけくんが宝石を受け取る時刻を出力
    for i in range(N):
        print(A[i])

=======
Suggestion 8

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    for i in range(n):
        print(t[i] + s[(i + 1) % n] - t[(i + 1) % n])

=======
Suggestion 9

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    # すぬけ君の宝石を貰う時刻
    # 初期値はT_i
    recieve = T[:]

    # すぬけ君の宝石を渡す時刻
    give = [0] * N

    # すぬけ君の宝石を渡す時刻を計算する
    for i in range(N):
        give[i] = recieve[i] + S[i]

    # すぬけ君の宝石を貰う時刻を計算する
    for i in range(N):
        # すぬけ君の宝石を渡す時刻よりも
        # すぬけ君の宝石を貰う時刻が大きい場合
        if recieve[(i + 1) % N] < give[i]:
            # すぬけ君の宝石を渡す時刻を
            # すぬけ君の宝石を貰う時刻とする
            recieve[(i + 1) % N] = give[i]

    # すぬけ君の宝石を貰う時刻を出力する
    for i in range(N):
        print(recieve[i])

=======
Suggestion 10

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    T2 = list(T)
    for i in range(N):
        T2[(i+1)%N] = min(T2[(i+1)%N], T2[i] + S[i])
    for i in range(N):
        T[i] = min(T[i], T2[(i-1)%N] + S[(i-1)%N])
    for i in range(N):
        print(T[i])
