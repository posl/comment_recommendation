Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += A[i]
        if sum > T:
            print(i+1, T-(sum-A[i]))
            break
        elif sum == T:
            print(i+1, 0)
            break

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += A[i]
        if sum >= T:
            print(i+1, T - sum + A[i])
            return

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T)
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    if sum <= T:
        T = T % sum
    #print(T)
    for i in range(N):
        if T < A[i]:
            print(i+1, T)
            break
        else:
            T -= A[i]

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for a in A:
        sum += a
    r = T % sum
    for i in range(N):
        if r < A[i]:
            print(i+1, r)
            return
        else:
            r -= A[i]

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T, A)
    sum = 0
    for i in range(N):
        sum += A[i]
        if sum > T:
            print(i+1, T-(sum-A[i]))
            break

=======
Suggestion 6

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    play = T % sum_A
    for i in range(N):
        play -= A[i]
        if play <= 0:
            print(i + 1, A[i] + play)
            break

=======
Suggestion 7

def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    total = sum(a)
    q,r = divmod(t,total)
    ans = 0
    for i in range(n):
        r -= a[i]
        if r < 0:
            ans = i+1
            break
    print(ans,r+a[i])

=======
Suggestion 8

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    # 1曲の長さの合計
    sum_a = sum(A)
    # 何周したか
    cnt = T // sum_a
    # 余り
    amari = T - cnt * sum_a

    # 余りを引いたときの曲の番号
    for i in range(N):
        amari -= A[i]
        if amari < 0:
            print(i+1, A[i]+amari)
            break

=======
Suggestion 9

def main():
    #input
    N, T = map(int, input().split())
    As = list(map(int, input().split()))

    #compute
    #Aの合計値
    Asum = sum(As)
    #Aの合計値で割った余り
    T %= Asum
    #Aの合計値で割った商
    Quotient = T // Asum
    #TをAの合計値で割った余りで割った商
    Quotient2 = Quotient // N
    #TをAの合計値で割った余りで割った余り
    Remainder = Quotient % N
    #TをAの合計値で割った余りで割った余りをAの合計値で割った商にかけたもの
    Quotient3 = Remainder * Quotient2
    #TをAの合計値で割った余りで割った余りをAの合計値で割った商にかけたものをAの合計値で割った余りに足したもの
    Remainder2 = Quotient3 + (T % Asum)
    #TをAの合計値で割った余りで割った余りをAの合計値で割った商にかけたものをAの合計値で割った余りに足したものをAの合計値で割った余りで割った商
    Quotient4 = Remainder2 // Asum
    #TをAの合計値で割った余りで割った余りをAの合計値で割った商にかけたものをAの合計値で割った余りに足したものをAの合計値で割った余りで割った余り
    Remainder3 = Remainder2 % Asum

=======
Suggestion 10

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    # プレイリストの曲数
    # 曲iの長さ
    # プレイリストを再生してからの時間
    # プレイリストを再生してからの時間を曲の長さで割った余り
    # プレイリストを再生してからの時間を曲の長さで割った商
    # プレイリストを再生してからの時間を曲の長さで割った商 + 1
    # プレイリストを再生してからの時間を曲の長さで割った商 + 1の曲の長さ
    # プレイリストを再生してからの時間を曲の長さで割った商 + 1の曲の長さ - プレイリストを再生してからの時間を曲の長さで割った余り
    # プレイリストを再生してからの時間を曲の長さで割った商 + 1の曲の長さ - プレイリストを再生してからの時間を曲の長さで割った余り + 1
    # プレイリストを再生してからの時間を曲の長さで割った商 + 1の曲の長さ - プレイリストを再生してからの時間を曲の長さで割った余り + 1の曲番号
    # プレイリストを再生してからの時間を曲の長さで割った商 + 1の曲の長さ - プレイリストを再生してからの時間を曲の長さで割った余り + 1の曲番号の曲の長さ
    # プレイリストを再生して
