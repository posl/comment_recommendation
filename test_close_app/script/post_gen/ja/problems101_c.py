Synthesizing 10/10 solutions

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] != i+1:
            cnt += 1
    if cnt%K == 0:
        print(cnt//K)
    else:
        print(cnt//K+1)

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - K + 1):
        if A[i] != i + 1:
            ans += 1
    print(ans)

=======

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i] == a[i - 1] + 1:
            ans += 1
    print((ans + k - 2) // (k - 1))

=======

def main():
    #入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    #連続するK個の要素の中の最小値を求める
    min_list = []
    for i in range(N-K+1):
        min_list.append(min(A[i:i+K]))
    
    #答え
    print(min(min_list))

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    #print(N, K)
    #print(A)
    A.sort()
    #print(A)

    # 連続した K 個の要素を選ぶ
    # その後，選んだ要素それぞれの値を，選んだ要素の中の最小値で置き換える
    # この操作を何回か繰り返すことで，この数列の要素をすべて等しくしたい

    # 連続した K 個の要素を選ぶ
    # その後，選んだ要素それぞれの値を，選んだ要素の中の最小値で置き換える
    # この操作を何回か繰り返すことで，この数列の要素をすべて等しくしたい
    # 連続した K 個の要素を選ぶ
    # その後，選んだ要素それぞれの値を，選んだ要素の中の最小値で置き換える
    # この操作を何回か繰り返すことで，この数列の要素をすべて等しくしたい
    # 連続した K 個の要素を選ぶ
    # その後，選んだ要素それぞれの値を，選んだ要素の中の最小値で置き換える
    # この操作を何回か繰り返すことで，この数列の要

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    #連続するK個の要素を選ぶ
    #選んだ要素それぞれの値を，選んだ要素の中の最小値で置き換える
    #選んだ要素の中の最小値を求める
    #選んだ要素の中の最小値と同じ値を持つ要素の数を求める
    #選んだ要素の中の最小値と同じ値を持つ要素の数をKで割った商を求める
    #選んだ要素の中の最小値と同じ値を持つ要素の数をKで割った余りを求める
    #選んだ要素の中の最小値と同じ値を持つ要素の数をKで割った商を求める
    #選んだ要素の中の最小値と同じ値を持つ要素の数をKで割った余りが0のときは
    #選んだ要素の中の最小値と同じ値を持つ要素の数をKで割った商を求める
    #選んだ要素の中の最小値と同じ値を持つ要素の数をKで割った余りが0でないときは
    #選んだ要素の中の最小値と同じ値を持つ要素の数をKで割った商に1を足した数を求める
    #選んだ要素の中の最小値と同じ値を持つ要素の数をKで割った商に1を足した数を合計する

    #選んだ要素の中の最小値と同じ値を持つ要

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    if N <= K:
        print(1)
        return
    # 1. AをK個のグループに分ける
    # 2. それぞれのグループについて、最小値を求める
    # 3. それぞれのグループについて、最小値になるまでの操作回数を求める
    # 4. それぞれのグループの操作回数の最大値を出力する
    # 5. 1-4を繰り返す

    # 1. AをK個のグループに分ける
    # 2. それぞれのグループについて、最小値を求める
    # 3. それぞれのグループについて、最小値になるまでの操作回数を求める
    # 4. それぞれのグループの操作回数の最大値を出力する
    # 5. 1-4を繰り返す
    # 1. AをK個のグループに分ける
    # 2. それぞれのグループについて、最小値を求める
    # 3. それぞれのグループについて、最小値になるまでの操作回数を求める
    # 4. それぞれのグループの操作回数の最大値を出力する
    # 5. 1-4を繰り返す
    # 1. AをK個のグループに分ける
    # 2. それぞれのグループについて、最小値を求め

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 各要素の個数を数える
    count = [0] * N
    for a in A:
        count[a-1] += 1

    # 各要素の個数を降順にソートする
    count.sort(reverse=True)

    # 最大の個数を求める
    max_count = count[0]

    # 最大の個数から K 個ずつ引いていく
    ans = 0
    for i in range(1, N):
        if max_count - count[i] >= K:
            ans += count[i]
            max_count -= count[i]
        else:
            break

    print(ans)

=======

def main():
    #入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #各要素の個数をカウント
    counter_A = [0] * N
    for i in range(N):
        counter_A[A[i] - 1] += 1
    #各要素の個数をソート
    counter_A.sort()
    #最小値を求める
    min_A = counter_A[0]
    #最大値を求める
    max_A = counter_A[-1]
    #最小値と最大値の差を求める
    diff_A = max_A - min_A
    #最小値と最大値の差がKで割り切れる場合
    if diff_A % K == 0:
        #最小値と最大値の差をKで割る
        ans = diff_A // K
    #最小値と最大値の差がKで割り切れない場合
    else:
        #最小値と最大値の差をKで割った商に1を足す
        ans = diff_A // K + 1
    #出力
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #dp[i][j] := i番目までの要素で、最後の要素がjのときの最小操作回数
    #dp[i][j] = min(dp[i-K][1]~dp[i-K][j-1]) + 1
    dp = [[10**9] * (N+1) for i in range(N+1)]
    for i in range(1, N+1):
        dp[i][A[i-1]] = 0
    for i in range(1, N+1):
        for j in range(1, i+1):
            for k in range(max(1, j-K+1), j):
                dp[i][j] = min(dp[i][j], dp[i-K][k] + 1)
    print(min(dp[N]))
