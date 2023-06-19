Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find_root(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_root(par[x])
        return par[x]

=======
Suggestion 2

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 3

def find(x):
    if x == par[x]:
        return x
    par[x] = find(par[x])
    return par[x]

=======
Suggestion 4

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

=======
Suggestion 5

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 6

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    carriages = [i for i in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            # 1 x y：把车y的前面和车x的后面连接起来。
            # 可以保证：
            # x ≠ y
            # 就在这个查询之前，没有火车连接到x号车的后面；
            # 就在这个查询之前，没有火车连接到y车的前面；
            # 就在这次查询之前，车x和车y属于不同的连接部件。
            x = query[1] - 1
            y = query[2] - 1
            if carriages[x] != carriages[y]:
                for j in range(N):
                    if carriages[j] == carriages[y]:
                        carriages[j] = carriages[x]
        elif query[0] == 2:
            # 2 x y：将车y的车头与车x的车尾断开连接。
            # 可以保证：
            # x ≠ y；
            # 就在这个查询之前，车y的前面与车x的后面直接相连。
            x = query[1] - 1
            y = query[2] - 1
            if carriages[x] == carriages[y]:
                for j in range(N):
                    if carriages[j] == carriages[x]:
                        carriages[j] = j
        elif query[0] == 3:
            # 3 x:打印属于包含车x的连接部件的车的车号，从前到后。
            x = query[1] - 1
            result = []
            for j in range(N):
                if carriages[j] == carriages[x]:
                    result.append(str(j + 1))
            print(len(result), ' '.join(result))

=======
Suggestion 8

def main():
    n,q = map(int,input().split())
    p = list(range(n+1))
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    def union(x,y):
        px,py = find(x),find(y)
        if px != py:
            p[px] = py
    def same(x,y):
        return find(x) == find(y)
    ans = []
    for _ in range(q):
        c,*q = map(int,input().split())
        if c == 1:
            x,y = q
            union(x,y)
        elif c == 2:
            x,y = q
            if same(x,y):
                union(x,y-1)
                union(x+1,y)
        else:
            x = q[0]
            ans.append([i for i in range(1,n+1) if same(x,i)])
    for i in ans:
        print(len(i),*i)

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    ans = []
    train = [[] for _ in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1] - 1, query[2] - 1
            train[x].append(y)
            train[y].append(x)
        elif query[0] == 2:
            x, y = query[1] - 1, query[2] - 1
            train[x].remove(y)
            train[y].remove(x)
        elif query[0] == 3:
            x = query[1] - 1
            ans.append(train[x])
    for i in range(len(ans)):
        print(len(ans[i]), *ans[i])
