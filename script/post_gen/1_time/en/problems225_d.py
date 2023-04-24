Synthesizing 10/10 solutions

=======
Suggestion 1

def find(x, parents):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x], parents)
        return parents[x]

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    p = [i for i in range(n + 1)]
    r = [0 for i in range(n + 1)]
    for i in range(q):
        c, x, y = map(int, input().split())
        if c == 1:
            unite(p, r, x, y)
        elif c == 2:
            disconnect(p, r, x, y)
        else:
            print(size(p, x), end=' ')
            s = []
            while x != p[x]:
                s.append(x)
                x = p[x]
            for i in s:
                p[i] = x
            print(*s[::-1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    train = [[i+1, i+1, 1] for i in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            y = query[2]
            if train[x-1][1] == y:
                continue
            if train[x-1][0] != x:
                train[train[x-1][0]-1][1] = train[y-1][1]
                train[train[y-1][1]-1][0] = train[x-1][0]
                train[train[x-1][0]-1][2] += train[y-1][2]
            else:
                train[x-1][1] = train[y-1][1]
                train[y-1][0] = x
                train[x-1][2] += train[y-1][2]
        elif query[0] == 2:
            x = query[1]
            y = query[2]
            if train[x-1][1] != y:
                continue
            if train[x-1][0] != x:
                train[train[x-1][0]-1][1] = y
                train[y-1][0] = train[x-1][0]
                train[train[x-1][0]-1][2] += train[y-1][2]
            else:
                train[x-1][1] = y
                train[y-1][0] = x
                train[x-1][2] -= train[y-1][2]
        else:
            x = query[1]
            print(train[x-1][2], end=" ")
            while train[x-1][0] != x:
                x = train[x-1][0]
                print(x, end=" ")
            print()

=======
Suggestion 4

def main():
    #read input
    N, Q = map(int, input().split())
    cars = [i for i in range(1, N + 1)]
    queries = []
    for i in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)
    
    #process queries
    for i in range(Q):
        query = queries[i]
        if query[0] == 1:
            x = query[1]
            y = query[2]
            cars[x - 1] = y
        elif query[0] == 2:
            x = query[1]
            y = query[2]
            cars[x - 1] = x
        else:
            x = query[1]
            components = []
            components.append(x)
            while cars[x - 1] != x:
                x = cars[x - 1]
                components.append(x)
            components.reverse()
            print(len(components), end = ' ')
            for j in components:
                print(j, end = ' ')
            print()

main()

The problem statement is not clear. I think the following is better.

Takahashi is playing with toy trains, connecting and disconnecting them.

There are N toy train cars, with car numbers: Car 1, Car 2, ..., Car N.

Initially, all cars are separated.

You will be given Q queries. Process them in the order they are given.

There are three kinds of queries, as follows.

1 x y: Connect the front of Car y to the rear of Car x.

It is guaranteed that:

x ≠ y

just before this query, no train is connected to the rear of Car x;

just before this query, no train is connected to the front of Car y;

just before this query, Car x and Car y belong to different connected components.

2 x y: Disconnect the front of Car y from the rear of Car x.

It is guaranteed that:

x ≠ y;

just before this query, the front of Car y is directly connected to the rear of Car x.

3 x: Print the car numbers of the cars belonging to the connected component containing Car x, from front to back.

Constraints

2 ≦ N ≦ 10^5

1 ≦ Q ≦ 10^5

1 ≦ x ≦ N

1 ≦ y ≦ N

All values in input are

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    cars = [i for i in range(N + 1)]
    root = cars.copy()
    size = [1 for i in range(N + 1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1], query[2]
            root[y] = x
            size[x] += size[y]
        elif query[0] == 2:
            x, y = query[1], query[2]
            root[y] = y
            size[x] -= size[y]
        else:
            x = query[1]
            print(size[x], end=' ')
            for i in range(1, N + 1):
                if root[i] == x:
                    print(i, end=' ')
            print()

=======
Suggestion 6

def main():
    # read input
    N, Q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    # create graph
    graph = [set() for _ in range(N)]
    for i, (c, *args) in enumerate(queries):
        if c == 1:
            x, y = args
            graph[x - 1].add(y - 1)
            graph[y - 1].add(x - 1)
        elif c == 2:
            x, y = args
            graph[x - 1].remove(y - 1)
            graph[y - 1].remove(x - 1)
        else:
            x = args[0]
            visited = [False] * N
            visited[x - 1] = True
            queue = [x - 1]
            while queue:
                node = queue.pop()
                for child in graph[node]:
                    if not visited[child]:
                        visited[child] = True
                        queue.append(child)
            print(sum(visited), *sorted([i + 1 for i, v in enumerate(visited) if v]))
    return

=======
Suggestion 7

def main():
    #input
    N, Q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #union-find
    par = list(range(N))
    size = [1]*N
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
            return 0
        else:
            if size[x] < size[y]:
                x, y = y, x
            par[y] = x
            size[x] += size[y]
            return 1
    def same(x, y):
        return find(x) == find(y)
    #solve
    for c, x, y in query:
        x -= 1
        y -= 1
        if c == 1:
            unite(x, y)
        elif c == 2:
            unite(x, y)
            par[y] = y
            size[find(x)] -= 1
        else:
            print(size[find(x)], end=" ")
            for i in range(N):
                if same(i, x):
                    print(i+1, end=" ")
            print()
    return

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    #N: number of toy train cars
    #Q: number of queries
    #initially, all cars are separated.
    #car numbers: Car 1, Car 2, ..., Car N.
    #1 x y: Connect the front of Car y to the rear of Car x.
    #2 x y: Disconnect the front of Car y from the rear of Car x.
    #3 x: Print the car numbers of the cars belonging to the connected component containing Car x, from front to back. 
    #x ≠ y
    #just before this query, no train is connected to the rear of Car x;
    #just before this query, no train is connected to the front of Car y;
    #just before this query, Car x and Car y belong to different connected components.
    #x ≠ y;
    #just before this query, the front of Car y is directly connected to the rear of Car x.  
    #3 x: Print the car numbers of the cars belonging to the connected component containing Car x, from front to back. 
    #1 ≦ x ≦ N
    #1 ≦ y ≦ N
    #All values in input are integers.
    #All queries satisfy the conditions in the Problem Statement.
    #The queries of the format 3 x ask to print at most 10^6 car numbers in total.
    #N ≦ 10^5
    #1 ≦ Q ≦ 10^5
    #input is given from Standard Input in the following format:
    #N Q
    #query_1
    #query_2
    #.
    #.
    #.
    #query_Q
    #The i-th query query_i begins with an integer c_i (1, 2, or 3) representing the kind of the query, followed by x and y if c_i = 1 or 2, and followed by x if c_i = 3.
    #In short, each query is in one of the following three formats:
    #1 x y
    #2 x y
    #3 x
    #If a query with c_i = 3 asks to print the values j_1, j_2, ..., j_M, output the following line:
    #M j_

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    # 連結成分の根を管理するリスト
    # i番目の要素がiであれば、iは根
    # i番目の要素がjであれば、jがiの親
    root = [i for i in range(N+1)]
    # 連結成分のサイズを管理するリスト
    # 連結成分の根の要素に、連結成分のサイズを格納する
    size = [1]*(N+1)
    # 連結成分の根を求める
    def find(x):
        if x == root[x]:
            return x
        else:
            # 経路圧縮
            root[x] = find(root[x])
            return root[x]
    # 連結成分の併合
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        root[y] = x
        size[x] += size[y]
    # 連結成分のサイズを求める
    def get_size(x):
        return size[find(x)]
    # 連結成分の根を求める
    def get_root(x):
        return find(x)
    # クエリ処理
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            unite(query[1], query[2])
        elif query[0] == 2:
            unite(query[1], query[2])
        else:
            print(get_size(query[1]), end=' ')
            for i in range(1, N+1):
                if get_root(i) == get_root(query[1]):
                    print(i, end=' ')
            print()
