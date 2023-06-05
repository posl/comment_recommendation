Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find_set(x):
    global p
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

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
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    p = [i for i in range(n+1)]
    head = [i for i in range(n+1)]
    tail = [i for i in range(n+1)]
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            p[head[query[2]]] = p[tail[query[1]]]
            p[tail[query[1]]] = query[2]
            tail[head[query[2]]] = tail[query[1]]
            head[query[2]] = head[query[1]]
            head[query[1]] = 0
            tail[query[1]] = 0
        elif query[0] == 2:
            p[tail[query[2]]] = p[tail[query[1]]]
            p[head[query[1]]] = query[2]
            tail[query[1]] = 0
            tail[query[2]] = tail[query[1]]
            head[query[1]] = 0
        else:
            print(' '.join(map(str, [i for i in range(1, n+1) if p[i] == p[query[1]]])))

=======
Suggestion 5

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 6

def main():
    N,Q = map(int,input().split())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))

    #print(N,Q)
    #print(query)

    # 连接部件
    parts = []
    for i in range(N):
        parts.append([i+1])

    #print(parts)

    # 处理查询
    for i in range(Q):
        if query[i][0] == 1:
            # 1 x y：把车y的前面和车x的后面连接起来。
            # 可以保证：
            # x ≠ y
            # 就在这个查询之前，没有火车连接到x号车的后面；
            # 就在这个查询之前，没有火车连接到y车的前面；
            # 就在这次查询之前，车x和车y属于不同的连接部件。
            x = query[i][1]
            y = query[i][2]
            #print("1",x,y)
            #print(parts)
            #print(parts[x-1])
            #print(parts[y-1])
            #print(parts[x-1] == parts[y-1])
            if parts[x-1] != parts[y-1]:
                parts[x-1] = parts[x-1] + parts[y-1]
                parts[y-1] = parts[x-1]
            #print(parts)

        if query[i][0] == 2:
            # 2 x y：将车y的车头与车x的车尾断开连接。
            # 可以保证：
            # x ≠ y；
            # 就在这个查询之前，车y的前面与车x的后面直接相连。
            x = query[i][1]
            y = query[i][2]
            #print("2",x,y)
            #print(parts)
            #print(parts[x-1])
            #print(parts[y-1])
            #print(parts[x-1] == parts[y-1])
            if parts[x-1] == parts[y-1]:
                parts[x-1] = [x]
                parts[y-1] = [y]
            #print(parts)

        if query[i][0]

=======
Suggestion 7

def get_input():
    n, q = map(int, input().split())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    return n, q, query

=======
Suggestion 8

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
