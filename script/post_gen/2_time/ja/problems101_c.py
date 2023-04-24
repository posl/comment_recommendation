Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # N, K = 8, 3
    # A = [7, 3, 1, 8, 4, 6, 2, 5]
    # print(N, K, A)

    # 1. 連続するK個の要素を選ぶ
    # 2. 選んだ要素それぞれの値を，選んだ要素の中の最小値で置き換える
    # 3. スヌケ君は，上の操作を何回か繰り返すことで，この数列の要素をすべて等しくしたいです．

    # 連続するK個の要素を選ぶ
    # 1. 連続するK個の要素の中の最小値を探す
    # 2. 連続するK個の要素の中の最小値で全ての要素を置き換える
    # 3. 1. 2. を繰り返す

    # 連続するK個の要素の中の最小値を探す
    # 1. 連続するK個の要素を選び、その最小値を探す
    # 2. 1. を繰り返す

    # 連続するK個の要素を選び、その最小値を探す
    # 1. K個の要素を選ぶ
    # 2. 1. を繰り返す

    # K個の要素を選ぶ
    # 1. Aの先頭からK個の要素を取り出す
    # 2. 取り出した要素の中の最小値を探す
    # 3. 1.

=======
Suggestion 2

def main():
    #入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #連続したK個の要素を選ぶ
    #最小値で置き換える
    #すべて等しくしたい
    #操作の回数の最小値を求める
    #最小値を更新する
    #最小値が変わらなくなるまで繰り返す
    #最小値を出力する
    pass

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 連続したK個の要素を選ぶ
    # 選んだ要素それぞれの値を，選んだ要素の中の最小値で置き換える
    # この操作を何回か繰り返すことで，この数列の要素をすべて等しくしたい
    # この問題の制約の下，このようなことは必ず可能であることが証明できます．
    # 必要な操作の回数の最小値を求めてください．
    # この問題の制約の下，このようなことは必ず可能であることが証明できます．
    # 必要な操作の回数の最小値を求めてください．
    # この問題の制約の下，このようなことは必ず可能であることが証明できます．
    # 必要な操作の回数の最小値を求めてください．
    # この問題の制約の下，このようなことは必ず可能であることが証明できます．
    # 必要な操作の回数の最小値を求めてください．
    # この問題の制約の下，このようなことは必ず可能であることが証明できます．
    # 必要な操作の回数の最小値を求めてください．
    # この問題の制約の下，このようなことは必ず可能であることが証明できます．
    # 必要な操作の回数の最小値を求めてください．
    # この問題の制約の下，

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    #N, K = 4, 3
    #A = [2, 3, 1, 4]
    #print(N, K)
    #print(A)
    #N, K = 3, 3
    #A = [1, 2, 3]
    #print(N, K)
    #print(A)
    #N, K = 8, 3
    #A = [7, 3, 1, 8, 4, 6, 2, 5]
    #print(N, K)
    #print(A)
    #A = [1, 2, 3, 4]
    #print(A)
    #print(len(A))
    #print(A[0:K])
    #print(A[K-1])
    #print(A[K:len(A)])
    #print(A[K-1] + A[K:len(A)])
    #A = [1, 1, 1, 1]
    #print(A)
    #print(len(A))
    #print(A[0:K])
    #print(A[K-1])
    #print(A[K:len(A)])
    #print(A[K-1] + A[K:len(A)])
    #A = [1, 1, 1, 4]
    #print(A)
    #print(len(A))
    #print(A[0:K])
    #print(A[K-1])
    #print(A[K:len(A)])
    #print(A[K-1] + A[K:len(A)])
    #A = [1, 1, 1, 1, 1]
    #print(A)
    #print(len(A))
    #print(A[0:K])
    #print(A[K-1])
    #print(A[K:len(A)])
    #print(A[K-1] + A[K:len(A)])
    #A = [1, 1, 1, 1, 4]
    #print(A)
    #print(len(A))
    #print(A[0:K])
    #print(A[K-1])
    #print(A[K:len(A)])
    #print(A[K-1] + A[K:len

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    ans = 0
    for i in range(n):
        if a[i] == i + 1:
            ans += 1
            for j in range(i + 1, i + k):
                if j == n: break
                if a[j] == j + 1:
                    ans += 1
                    break
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-K])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 1, 2, ..., N に並び替える
    B = sorted(A)
    # 連続する K 個の要素を選ぶ
    # 選んだ要素それぞれの値を，選んだ要素の中の最小値で置き換える
    # この操作を何回か繰り返すことで，この数列の要素をすべて等しくしたい
    # 必要な操作の回数の最小値を求める
    # この問題の制約の下，このようなことは必ず可能であることが証明できる
    # 操作の回数の最小値を求める
    # 選んだ要素の中の最小値で置き換える
    # 選んだ要素の中の最小値は，選んだ要素の中の最大値と同じになる
    # 選んだ要素の中の最大値は，選んだ要素の中の最小値と同じになる
    # 選んだ要素の中の最小値は，選んだ要素の中の最大値と同じになる
    # 選ん

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 1. A の要素を K 個ずつに分割する
    # 2. 分割した要素の中で最小値を求める
    # 3. 最小値を K 個の要素の中での最大値を求める
    # 4. 3. の最大値を求める
    # 5. 4. で求めた最大値を A の要素数で割った商が答え
    # 5. の商が 0 なら 1 にする
    ans = 0
    for i in range(0, N, K):
        ans = max(ans, min(A[i:i+K]))
    print((N - ans + K - 1) // K)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #最小値を取る数に変換
    for i in range(N):
        A[i] -= 1
    #数列の長さをKで割った余りを求める
    mod = N % K
    #余りが0のときは、Kで割った数を求める
    if mod == 0:
        mod = N // K
    #余りが0でないときは、Kで割った数に1を足す
    else:
        mod = N // K + 1
    #余りを出力する
    print(mod)
