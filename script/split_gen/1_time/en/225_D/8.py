def main():
    N, Q = map(int, input().split())
    #parent[i] = iならばiは根
    #iの親の番号をparent[i]に格納
    parent = list(range(N))
    #rank[i] = iの木の深さ
    rank = [0] * N
    #size[i] = iの連結成分のサイズ
    size = [1] * N
    def root(x):
        #根まで再帰的に辿る
        if parent[x] == x:
            return x
        else:
            parent[x] = root(parent[x])
            return parent[x]
    def unite(x, y):
        #xとyの木を併合
        x = root(x)
        y = root(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            parent[x] = y
            size[y] += size[x]
        else:
            parent[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1
    def same(x, y):
        #xとyが同じ連結成分に属するかどうか
        return root(x) == root(y)
    def size(x):
        #xの連結成分のサイズ
        return size[root(x)]
    def members(x):
        #xの連結成分のメンバー
        root = root(x)
        return [i for i in range(N) if root(i) == root]
    def roots():
        #全ての根のリスト
        return [i for i, x in enumerate(parent) if i == x]
    def group_count():
        #連結成分の数
        return len(roots())
    def all_group_members():
        #{根: [連結成分のメンバーのリスト], ...}の辞書
        return {r: members(r) for r in roots()}
    def print_group():
        #全ての連結成分を出力
        print(all_group_members())
    for _ in range(Q):
        c, x, y = map(int
