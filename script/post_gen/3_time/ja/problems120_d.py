Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.reverse()
    B.reverse()

    # Union-Find
    par = [i for i in range(N+1)]
    rank = [0] * (N+1)
    size = [1] * (N+1)
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        elif rank[x] < rank[y]:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1
        return True
    def same(x, y):
        return find(x) == find(y)

    # 初期状態の不便さ
    ans = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if same(i, j):
                continue
            ans += size[i] * size[j]
            unite(i, j)
    print(ans)

    for i in range(M-1):
        a = A[i]
        b = B[i]
        if same(a, b):
            continue
        ans -= size[find(a)] * size[find(b)]
        unite(a, b)
        print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.reverse()
    B.reverse()
    union = UnionFind(N)
    ans = [0] * M
    for i in range(M):
        ans[i] = union.size(A[i] - 1) * union.size(B[i] - 1)
        union.union(A[i] - 1, B[i] - 1)
    ans.reverse()
    for i in range(M):
        ans[i] -= union.size(A[i] - 1) * union.size(B[i] - 1)
    for i in range(M):
        ans[i] += ans[i - 1]
    for i in range(M):
        print(ans[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1

    # 連結成分の個数
    ans = [0] * M
    ans[M-1] = N * (N-1) // 2
    # 各連結成分のサイズ
    size = [1] * N
    # 連結成分の根
    root = list(range(N))

    def root_of(x):
        if root[x] == x:
            return x
        else:
            root[x] = root_of(root[x])
            return root[x]

    def unite(x, y):
        x = root_of(x)
        y = root_of(y)
        if x == y:
            return
        ans[M-1] -= size[x] * size[y]
        if size[x] < size[y]:
            x, y = y, x
        root[y] = x
        size[x] += size[y]

    for i in range(M-1, 0, -1):
        ans[i-1] = ans[i]
        if root_of(A[i]) != root_of(B[i]):
            ans[i-1] -= 1
            unite(A[i], B[i])

    for i in range(M):
        print(ans[i])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print(A)
    #print(B)
    
    #初期状態の不便さ
    ans = (N-1)*(N-2)//2
    #print(ans)
    
    #各島が何個の島とつながっているか
    #島番号をインデックスとして使うため、0番目をダミーとして1から使う
    connect = [0] * (N+1)
    #print(connect)
    
    #各島が何個の島とつながっているかを調べる
    for i in range(M):
        connect[A[i]] += 1
        connect[B[i]] += 1
    #print(connect)
    
    #各島が何個の島とつながっているかをもとに不便さを計算する
    for i in range(M):
        #print(i)
        #print(ans)
        #print(connect[A[i]])
        #print(connect[B[i]])
        ans -= connect[A[i]]-1
        ans -= connect[B[i]]-1
        connect[A[i]] = 0
        connect[B[i]] = 0
        print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * M
    ans[M-1] = N*(N-1)//2
    for i in range(M-1):
        a, b = AB[i]
        if a > b:
            a, b = b, a
        ans[M-i-2] = ans[M-i-1] - (N-a+1)*(N-b+1)//2
    print('

'.join(map(str, ans)))

=======
Suggestion 6

def main():
    import sys
    readline = sys.stdin.readline
    from collections import defaultdict
    N, M = map(int, readline().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, readline().split())
    A.reverse()
    B.reverse()
    #print(A)
    #print(B)
    d = defaultdict(int)
    for i in range(1, N+1):
        d[i] = 1
    #print(d)
    ans = [0]*M
    for i in range(M):
        ans[M-i-1] = (N*(N-1))//2 - (N-d[A[i]])*(N-d[B[i]])
        d[A[i]] += 1
        d[B[i]] += 1
    for i in range(M):
        print(ans[i])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    # N:島の数, M:橋の数
    bridge = [list(map(int, input().split())) for _ in range(M)]
    # bridge:橋の情報
    # bridge[i][0]:橋iの島A
    # bridge[i][1]:橋iの島B
    # bridge[i][2]:橋iの崩落フラグ(0:崩落前, 1:崩落後)
    # bridge[i][3]:橋iの崩落後の不便さ

    # 島の数がNの場合、最大不便さはN-1
    # これを初期値として設定する
    inconvenience = N - 1

    # 橋の情報を逆順に取得する
    for i in range(M - 1, -1, -1):
        # 橋iが崩落していない場合
        if bridge[i][2] == 0:
            # 橋iが崩落したことを記録する
            bridge[i][2] = 1
            # 橋iの崩落後の不便さを記録する
            bridge[i][3] = inconvenience
            # 橋iの島Aから島Bを経由して島Aに行く場合の不便さを計算する
            # 橋iの島Aから島Bを経由して島Aに行く場合の不便さは
            # 橋iの島Aから島Bを経由して島Aに行く場合の不便さ + 1
            inconvenience += 1
        # 橋iが崩落している場合
        else:
            # 橋iの崩落後の不便さを記録

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(M)]
    bridge = bridge[::-1]
    #print(bridge)
    #print(N, M)
    #print(bridge)
    #print(bridge[0][0])
    #print(bridge[0][1])
    #print(bridge[1][0])
    #print(bridge[1][1])
    #print(bridge[2][0])
    #print(bridge[2][1])
    #print(bridge[3][0])
    #print(bridge[3][1])
    #print(bridge[4][0])
    #print(bridge[4][1])
    #print(bridge[5][0])
    #print(bridge[5][1])
    #print(bridge[6][0])
    #print(bridge[6][1])
    #print(bridge[7][0])
    #print(bridge[7][1])
    #print(bridge[8][0])
    #print(bridge[8][1])
    #print(bridge[9][0])
    #print(bridge[9][1])
    
    #print(bridge[0][0])
    #print(bridge[0][1])
    #print(bridge[1][0])
    #print(bridge[1][1])
    #print(bridge[2][0])
    #print(bridge[2][1])
    #print(bridge[3][0])
    #print(bridge[3][1])
    #print(bridge[4][0])
    #print(bridge[4][1])
    #print(bridge[5][0])
    #print(bridge[5][1])
    #print(bridge[6][0])
    #print(bridge[6][1])
    #print(bridge[7][0])
    #print(bridge[7][1])
    #print(bridge[8][0])
    #print(bridge[8][1])
    #print(bridge[9][0])
    #print(bridge[9][1])
    
    #print(bridge[0][0])
    #print(bridge[0][1])
    #print(bridge[1][0])
    #print(bridge[1][1])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(M)]
    bridge.reverse()
    # print(bridge)

    # 連結成分の個数
    cnt = N
    # 連結成分の個数を数える
    # 連結成分の個数が1になるまで繰り返す
    # 連結成分の個数が1になると、それ以降の橋の崩落は不便さが増加しない
    # 連結成分の個数が1になるまでの橋の崩落回数を数える
    # 連結成分の個数が1になるまでの橋の崩落回数を、連結成分の個数で割る
    # 連結成分の個数が1になるまでの橋の崩落回数を、連結成分の個数で割った余りを、連結成分の個数で割る
    # 連結成分の個数が1になるまでの橋の崩落回数を、連結成分の個数で割った余りを、連結成分の個数で割った値を、連結成分の個数で割る
    # 連結成分の個数が1になるまでの橋の崩落回数を、連結成分の個数で割った余りを、連結成分の個数で割った値を、連結成分の個数で割った値を、連結成分の個数で割る
    # 連結成分の個数が1になるま

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    # 連結成分の個数を管理する
    # 連結成分の個数が増えると不便さが増える
    # 連結成分の個数が減ると不便さが減る
    # 連結成分の個数は、島の個数から1引いた値
    # つまり、島の個数 - 1 が連結成分の個数
    # 連結成分の個数が増えると不便さが増えるので、
    # 不便さは島の個数から連結成分の個数を引いた値
    # つまり、島の個数 - (連結成分の個数) が不便さ
    # 連結成分の個数が減ると不便さが減るので、
    # 不便さは島の個数から連結成分の個数を引いた値
    # つまり、島の個数 - (連結成分の個数) が不便さ
    # 以上のことから、不便さは島の個数 - 連結成分の個数
    # 連結成分の個数は、島の個数から1引いた値
    # つまり、島の個数 - 1 が連結成分の個数
    # 以上のことから、不便さは島の個数 - (島の個数 - 1)
    # つまり、不便さは島の個数 - (島の個数 - 1) = 1
    # つまり、不
