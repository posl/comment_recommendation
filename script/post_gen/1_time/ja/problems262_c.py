Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    minA = [0] * (N + 1)
    maxA = [0] * (N + 1)
    for i in range(N):
        minA[A[i]] = i + 1
        maxA[A[i]] = i + 1
    for i in range(1, N + 1):
        minA[i] = min(minA[i], minA[i - 1])
        maxA[N - i] = max(maxA[N - i], maxA[N - i + 1])
    ans = 0
    for i in range(1, N + 1):
        ans += maxA[i] - minA[i] + 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N + 1):
        if a[i - 1] == i:
            cnt += 1
        else:
            cnt += 0
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    ans = 0
    for i in range(1, N+1):
        if a[i] == i:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [1, 3, 2, 4]
    #N = 4
    #A = [5, 8, 2, 2, 1, 6, 7, 2, 9, 10]
    #N = 10
    #N = 5 × 10^5
    #1 ≦ a_i ≦ N  (1 ≦ i ≦ N)
    #A = [i for i in range(1, N+1)]
    #print(A)
    #print("N = {}".format(N))
    #print("A = {}".format(A))
    #print("len(A) = {}".format(len(A)))

    #min(a_i, a_j) = i
    #max(a_i, a_j) = j
    #i < j
    #1 ≦ i < j ≦ N
    #i = A[i-1]
    #j = A[j-1]
    #A = [1, 3, 2, 4]
    #A = [5, 8, 2, 2, 1, 6, 7, 2, 9, 10]
    #A = [i for i in range(1, N+1)]
    #print(A)
    #print("N = {}".format(N))
    #print("A = {}".format(A))
    #print("len(A) = {}".format(len(A)))

    #A = [1, 3, 2, 4]
    #A = [5, 8, 2, 2, 1, 6, 7, 2, 9, 10]
    #A = [i for i in range(1, N+1)]
    #print(A)
    #print("N = {}".format(N))
    #print("A = {}".format(A))
    #print("len(A) = {}".format(len(A)))

    #print("A = {}".format(A))
    #print("len(A) = {}".format(len(A)))
    #print("A[0] = {}".format(A[0]))
    #print("A[1] = {}".format(A[1]))
    #print("A[2

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    B = [0] * (N+1)
    for i in range(N):
        B[A[i]] += 1
    #print(B)
    ans = 0
    for i in range(1,N+1):
        if B[i] > 0:
            ans += B[i] * (B[i]-1) // 2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        min_i = a.index(i)
        max_i = a.index(i, min_i)
        if i == min(a[min_i:max_i+1]):
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # Aの各要素の個数をカウントする
    cnt = [0] * (N + 1)
    for i in range(N):
        cnt[A[i]] += 1

    # Aの各要素の個数の累積和を計算する
    sum_cnt = [0] * (N + 1)
    for i in range(N):
        sum_cnt[i + 1] = sum_cnt[i] + cnt[i + 1]

    # Aの各要素の個数の累積和を用いて、
    # min(A[i], A[j]) = i, max(A[i], A[j]) = j を満たす
    # (i, j) の個数を求める
    ans = 0
    for i in range(N):
        # A[i] = i の場合
        if A[i] == i + 1:
            ans += sum_cnt[N] - sum_cnt[i + 1]

        # A[i] > i の場合
        elif A[i] > i + 1:
            ans += cnt[A[i]]

    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # a[i]の値がiの個数を記録する
    # a[i]の値がiの個数を記録する
    cnt = [0] * (n+1)
    for i in range(n):
        cnt[a[i]] += 1

    # a[i]の値がiの個数を記録する
    cnt = [0] * (n+1)
    for i in range(n):
        cnt[a[i]] += 1

    # a[i]の値がiの個数を記録する
    cnt = [0] * (n+1)
    for i in range(n):
        cnt[a[i]] += 1

    # a[i]の値がiの個数を記録する
    cnt = [0] * (n+1)
    for i in range(n):
        cnt[a[i]] += 1

    # a[i]の値がiの個数を記録する
    cnt = [0] * (n+1)
    for i in range(n):
        cnt[a[i]] += 1

    # a[i]の値がiの個数を記録する
    cnt = [0] * (n+1)
    for i in range(n):
        cnt[a[i]] += 1

    # a[i]の値がiの個数を記録する
    cnt = [0] * (n+1)
    for i in range(n):
        cnt[a[i]] += 1

    # a[i]の値がiの個数を記録する
    cnt = [0] * (n+1)
    for i in range(n):
        cnt[a[i]] += 1

    # a[i]の値がiの個数を記録する
    cnt = [0] * (n+1)
    for i in range(n):
        cnt[a[i]] += 1

    # a[i]の値がiの個数を記録する
    cnt = [0] * (n

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #Aの値をkeyとした辞書を作成
    D = {i:[] for i in range(1,N+1)}
    for i in range(N):
        D[A[i]].append(i)
    #Aの値をkeyとした辞書から
    #最小値と最大値のindexを取得
    min_idx = [0]*N
    max_idx = [0]*N
    for i in range(1,N+1):
        min_idx[i-1] = D[i][0]
        max_idx[i-1] = D[i][-1]
    #min_idxの累積和を取得
    cumsum_min = [0]*(N+1)
    for i in range(1,N+1):
        cumsum_min[i] = cumsum_min[i-1] + min_idx[i-1]
    #max_idxの累積和を取得
    cumsum_max = [0]*(N+1)
    for i in range(1,N+1):
        cumsum_max[i] = cumsum_max[i-1] + max_idx[i-1]
    #min_idxとmax_idxを使って
    #条件を満たすi, jの組の数を求める
    ans = 0
    for i in range(1,N+1):
        ans += cumsum_max[i] - cumsum_max[i-1] * i
        ans += cumsum_min[N] - cumsum_min[i] - (N-i) * max_idx[i-1]
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    a = list(map(int, input().split()))

    #aの中の値をインデックスに持つリストを作成
    a_index = [0] * (N+1)
    for i in range(N):
        a_index[a[i]] = i

    #連続する数列の長さを格納するリスト
    length_list = [0] * (N+1)

    #aの中の値をインデックスに持つリストを左から順に見ていく
    for i in range(1, N+1):
        #aの中の値がインデックスと一致する場合
        if a_index[i] == i-1:
            #連続する数列の長さを格納するリストのインデックスをインクリメント
            length_list[i] += 1
        #aの中の値がインデックスと不一致の場合
        else:
            #連続する数列の長さを格納するリストのインデックスをインクリメント
            length_list[i] += 1
            #連続する数列の長さを格納するリストのインデックスをインクリメント
            length_list[a_index[i]+1] -= 1

    #連続する数列の長さの累積和を格納するリスト
    cumsum = [0] * (N+1)
    #連続する数列の長さの累積和を計算
    for i in range(1, N+1):
        cumsum[i] = cumsum[i-1] + length_list[i]

    #条件を満たす組の個数
    count = 0
    #連続する数列の長さの累積和を格納するリストを左から順に見ていく
    for i in range(1, N+1):
        #連続する数列の長さがインデックスと一
