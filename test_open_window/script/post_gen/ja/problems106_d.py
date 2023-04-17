Synthesizing 9/10 solutions

=======

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, M, Q)
    #print(LR)
    #print(PQ)
    
    #都市p_iから都市q_iまでの区間に走る区間が完全に含まれる列車の本数を求める
    #都市p_iから都市q_iまでの区間に走る区間が完全に含まれる列車の本数を求める
    #都市p_iから都市q_iまでの区間に走る区間が完全に含まれる列車の本数を求める
    #都市p_iから都市q_iまでの区間に走る区間が完全に含まれる列車の本数を求める
    #都市p_iから都市q_iまでの区間に走る区間が完全に含まれる列車の本数を求める
    #都市p_iから都市q_iまでの区間に走る区間が完全に含まれる列車の本数を求める
    #都市p_iから都市q_iまでの区間に走る区間が完全に含まれる列車の本数を求める
    #都市p_iから都市q_iまでの区間に走る区間が完全に含まれる列車の本数を求める
    #都市p_iから都市q_iまでの区間に走る区間が完全に含まれる列車の本数を求める
    #都市p_iから都市q_iまでの区間に走る区間が完全に含まれる列車の本数を求める
    #都市p_i

=======

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    #LR = [[1, 1], [1, 2], [2, 2]]
    #PQ = [[1, 2]]
    #LR = [[1, 6], [2, 9], [4, 5], [4, 7], [4, 7], [5, 8], [6, 6], [6, 7], [7, 9], [10, 10]]
    #PQ = [[1, 8], [1, 9], [1, 10], [2, 8], [2, 9], [2, 10], [3, 8], [3, 9], [3, 10], [1, 10]]
    #PQ = [[1, 10]]
    #LR = [[1, 5], [2, 8], [7, 10]]
    #PQ = [[1, 7], [3, 10]]
    #LR = [[1, 1], [1, 2], [2, 2]]
    #PQ = [[1, 2]]
    #N, M, Q = 2, 3, 1
    #LR = [[1, 1], [1, 2], [2, 2]]
    #PQ = [[1, 2]]
    #N, M, Q = 10, 3, 2
    #LR = [[1, 5], [2, 8], [7, 10]]
    #PQ = [[1, 7], [3, 10]]
    #N, M, Q = 10, 10, 10
    #LR = [[1, 6], [2, 9], [4, 5], [4, 7], [4, 7], [5, 8], [6, 6], [6, 7], [7, 9], [10, 10]]
    #PQ = [[1, 8], [1, 9

=======

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    # 区間に含まれる列車の本数を求める
    train = [[0] * (N + 1) for _ in range(N + 1)]
    for l, r in LR:
        train[l][r] += 1
    # 区間の累積和をとる
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            train[i][j] += train[i][j - 1]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            train[i][j] += train[i - 1][j]
    # 区間の累積和を利用して、区間に含まれる列車の本数を求める
    for p, q in PQ:
        print(train[q][q] - train[p - 1][q] - train[q][p - 1] + train[p - 1][p - 1])

=======

def main():
    N, M, Q = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    P = []
    Q = []
    for i in range(Q):
        p, q = map(int, input().split())
        P.append(p)
        Q.append(q)

=======

def main():
    n, m, q = map(int, input().split())
    l = [0] * m
    r = [0] * m
    for i in range(m):
        l[i], r[i] = map(int, input().split())
    p = [0] * q
    q1 = [0] * q
    for i in range(q):
        p[i], q1[i] = map(int, input().split())
    for i in range(q):
        ans = 0
        for j in range(m):
            if l[j] >= p[i] and r[j] <= q1[i]:
                ans += 1
        print(ans)

=======

def main():
    N, M, Q = map(int, input().split())
    train = [[0] * N for _ in range(N)]
    for _ in range(M):
        L, R = map(int, input().split())
        train[L - 1][R - 1] += 1
    for i in range(N):
        for j in range(N - 1):
            train[i][j + 1] += train[i][j]
    for i in range(N - 1):
        for j in range(N):
            train[i + 1][j] += train[i][j]
    for _ in range(Q):
        p, q = map(int, input().split())
        print(train[q - 1][q - 1] - train[p - 1][q - 1] - train[q - 1][p - 2] + train[p - 1][p - 2])

=======

def main():
    N, M, Q = map(int, input().split())
    train = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        L, R = map(int, input().split())
        train[L][R] += 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            train[i][j] = train[i][j] + train[i][j - 1]
    for _ in range(Q):
        p, q = map(int, input().split())
        ans = 0
        for i in range(p, q + 1):
            ans += train[i][q] - train[i][p - 1]
        print(ans)

=======

def main():
    N, M, Q = map(int, input().split())
    train = [0] * (N + 1)
    for i in range(M):
        L, R = map(int, input().split())
        train[L - 1] += 1
        train[R] -= 1
    for i in range(N):
        train[i + 1] += train[i]
    for i in range(Q):
        p, q = map(int, input().split())
        print(train[q] - train[p - 1])

=======

def main():
    # 1行目
    N, M, Q = map(int, input().split())
    # 2～M+1行目
    LR = [[int(x) for x in input().split()] for _ in range(M)]
    # M+2～M+Q+1行目
    PQ = [[int(x) for x in input().split()] for _ in range(Q)]

    # 都市のリスト
    cities = [0]*(N+1)
    # 都市の区間を記録するリスト
    cities_interval = [0]*(N+1)
    # 現在の都市の区間を記録するリスト
    interval = [0]*(N+1)
    # 区間の開始位置を記録するリスト
    interval_start = [0]*(N+1)
    # 区間の終了位置を記録するリスト
    interval_end = [0]*(N+1)
    # 区間の開始位置のインデックス
    start_index = 0
    # 区間の終了位置のインデックス
    end_index = 0
    # 区間の開始位置のインデックスを記録するリスト
    start_index_list = [0]*(N+1)
    # 区間の終了位置のインデックスを記録するリスト
    end_index_list = [0]*(N+1)
    # 区間の開始位置のインデックスのリストのインデックス
    start_index_list_index = 0
    # 区間の終了位置のインデックスのリストのインデックス
    end_index_list_index = 0

    # 区間の開始位置のインデックスを記録するリストを作成
    for i in range(M):
        start_index_list[LR[i][0]] = start_index
        start_index += 1
    # 区間の終了位置のインデックスを記録するリストを作成
    for i in range(M):
        end_index_list[LR[i][1]] = end_index
