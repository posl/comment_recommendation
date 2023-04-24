Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)

    # Aの要素をxにして、xがAの何番目に出てくるかを調べる
    # 重複する要素を考える
    # 重複する要素については、その要素の個数と出てきた位置を記録する
    # その後、XとKを入力した順に出力する
    # 重複する要素がない場合は、-1を出力する
    # 重複する要素がある場合は、K番目の要素を出力する
    # もしK番目の要素がない場合は、-1を出力する

    # 重複する要素を考える
    # 重複する要素については、その要素の個数と出てきた位置を記録する
    # その後、XとKを入力した順に出力する
    # 重複する要素がない場合は、-1を出力する
    # 重複する要素がある場合は、K番目の要素を出力する
    # もしK番目の要素がない場合は、-1を出力する
    # 重複する要素を考える
    # 重複する要素については、その要素の個数と出てきた位置を記録する
    # その後、XとKを入力した順に出力する
    # 重複する要素がない場合は、-1を出力する
    # 重複する要素がある場合は、K番

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)

    # リストの中のxの出現回数を数える
    # それをリストで返す
    def count_x(A, x):
        count = 0
        count_x = []
        for i in range(len(A)):
            if A[i] == x:
                count += 1
            count_x.append(count)
        return count_x

    # リストの中のxの出現回数を数える
    # それを辞書で返す
    def count_x2(A, x):
        count = 0
        count_x = {}
        for i in range(len(A)):
            if A[i] == x:
                count += 1
            count_x[A[i]] = count
        return count_x

    # リストの中のxの出現回数を数える
    # それを辞書で返す
    # ただし、リストの中のxの最初の出現回数は0とする
    def count_x3(A, x):
        count = 0
        count_x = {}
        for i in range(len(A)):
            if A[i] == x:
                count += 1
            count_x[A[i]] = count
        count_x[x] = 0
        return count_x

    # リストの中のxの出現回数を数える
    # それを辞書で返す
    # ただし、リストの中のxの最初の出現回数は0とする
    # また、リストの中のxの最後の出現回数はリストの長さとする
    def count_x4(A, x):
        count = 0
        count_x = {}
        for i in range(len(A)):
            if A[i] == x:
                count += 1
            count_x[A[i]] =

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)
    for i in range(Q):
        left = 0
        right = N
        while left < right:
            mid = (left + right) // 2
            if A[mid] == X[i]:
                if K[i] == 1:
                    right = mid
                else:
                    K[i] -= 1
                    left = mid + 1
            elif A[mid] < X[i]:
                left = mid + 1
            else:
                right = mid
        if left == N or A[left] != X[i]:
            print(-1)
        else:
            print(left + 1)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for _ in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)

    # A に含まれる数字の出現回数をカウント
    # A に含まれる数字の出現回数をカウント
    from collections import defaultdict
    d = defaultdict(int)
    for a in A:
        d[a] += 1

    # A の要素を前から順に見ていったときに、各数字の何回目に登場するかを記録
    # A の要素を前から順に見ていったときに、各数字の何回目に登場するかを記録
    d2 = defaultdict(list)
    for i, a in enumerate(A):
        d2[a].append(i)

    # 各クエリに対する答えを求める
    # 各クエリに対する答えを求める
    for x, k in zip(X, K):
        if d[x] < k:
            print(-1)
        else:
            print(d2[x][k-1] + 1)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * Q
    K = [0] * Q
    for i in range(Q):
        X[i], K[i] = map(int, input().split())
    #print("A:", A)
    #print("X:", X)
    #print("K:", K)

    #Aの各要素の値が最初に出現する位置を格納するリストを作成
    #Aの要素の値は最大で10^9なので10^9+1の要素数を持つリストを作成
    #Aの要素の値が出現しない場合は-1を格納する
    A_first = [-1] * (10**9+1)
    for i in range(N):
        if A_first[A[i]] == -1:
            A_first[A[i]] = i+1

    #print(A_first)

    #Xの各要素の値が最初に出現する位置を格納するリストを作成
    #Xの要素の値は最大で10^9なので10^9+1の要素数を持つリストを作成
    #Xの要素の値が出現しない場合は-1を格納する
    X_first = [-1] * (10**9+1)
    for i in range(Q):
        if X_first[X[i]] == -1:
            X_first[X[i]] = i+1

    #print(X_first)

    #Aの各要素の値がK回目に出現する位置を格納するリストを作成
    #Aの要素の値は最大で10^9なので10^9+1の要素数を持つリストを作成
    #Aの要素の値がK回目に出現しない場合は-1を格納する
    A_K = [-1] * (10**9+1)
    for i in range(N

=======
Suggestion 6

def main():
    # 入力
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)

    # 処理
    # 2次元配列にする
    A2 = [[0 for i in range(N+1)] for j in range(10**9+1)]
    for i in range(N):
        A2[A[i]][i+1] = 1

    # 累積和をとる
    for i in range(10**9+1):
        for j in range(N):
            A2[i][j+1] += A2[i][j]

    # 出力
    for i in range(Q):
        if A2[X[i]][N] < K[i]:
            print(-1)
        else:
            left = 0
            right = N
            while right - left > 1:
                mid = (left + right) // 2
                if A2[X[i]][mid] >= K[i]:
                    right = mid
                else:
                    left = mid
            print(right)

=======
Suggestion 7

def main():
    # input
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    Xs = [None] * Q
    Ks = [None] * Q
    for i in range(Q):
        Xs[i], Ks[i] = map(int, input().split())

    # compute
    As = [[As[i], i+1] for i in range(N)]
    As.sort()
    As.append([10**10, 0])

    # output
    for i in range(Q):
        l, r = 0, N
        while r-l > 1:
            m = (l+r)//2
            if As[m][0] <= Xs[i]:
                l = m
            else:
                r = m
        if As[l][0] == Xs[i]:
            print(As[l+Ks[i]-1][1])
        else:
            print(-1)

=======
Suggestion 8

def main():
    # input
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    Xs = [None]*Q
    Ks = [None]*Q
    for i in range(Q):
        Xs[i], Ks[i] = map(int, input().split())

    # compute
    Ds = {}
    for i, A in enumerate(As, 1):
        if A in Ds:
            Ds[A].append(i)
        else:
            Ds[A] = [i]
    ans = []
    for i in range(Q):
        X = Xs[i]
        K = Ks[i]
        if X in Ds and K <= len(Ds[X]):
            ans.append(Ds[X][K-1])
        else:
            ans.append(-1)

    # output
    for i in range(Q):
        print(ans[i])

=======
Suggestion 9

def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0 for _ in range(Q)]
    K = [0 for _ in range(Q)]
    for i in range(Q):
        X[i], K[i] = map(int, input().split())

    # Aの要素をxに分類
    # Aの要素に対応するindexを格納
    # 例) x = 1の要素のindexはindex[1]
    index = [[] for _ in range(10**9+1)]
    for i in range(N):
        index[A[i]].append(i)
    
    # Xの要素に対応するindexを格納
    # 例) Xの要素x = 1のindexはindex[1]
    index2 = [[] for _ in range(10**9+1)]
    for i in range(Q):
        index2[X[i]].append(i)

    # Xの要素に対応するindexを格納
    # 例) Xの要素x = 1のindexはindex[1]
    ans = [-1 for _ in range(Q)]
    for i in range(10**9+1):
        if len(index[i]) == 0:
            continue
        for j in index2[i]:
            if K[j] <= len(index[i]):
                ans[j] = index[i][K[j]-1] + 1

    for i in range(Q):
        print(ans[i])

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q, A, query)

    #Aの要素をa_1, a_2, ... と前から順に見ていったときに、数 x_i が k_i 回目に登場するのは A の前から何番目の要素を見たときかを出力してください。
    #    ただし条件を満たす要素が存在しない場合は -1 を出力してください。

    #Aの要素をa_1, a_2, ... と前から順に見ていったときに、数 x_i が k_i 回目に登場するのは A の前から何番目の要素を見たときかを出力してください。
    #    ただし条件を満たす要素が存在しない場合は -1 を出力してください。
    #Aの要素をa_1, a_2, ... と前から順に見ていったときに、数 x_i が k_i 回目に登場するのは A の前から何番目の要素を見たときかを出力してください。
    #    ただし条件を満たす要素が存在しない場合は -1 を出力してください。
    #Aの要素をa_1, a_2, ... と前から順に見ていったときに、数 x_i が k_i 回目に登場するのは A の前から何番目の要素を見たときかを出力してください。
    #    ただし条件を満たす要素が存在しない場合は -1 を出力してください。
    #Aの要素をa_1, a_2, ... と前から順に見ていったときに、数 x_i が k_i 回目に登場する
