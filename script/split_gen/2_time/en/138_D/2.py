def main():
    N, Q = list(map(int, input().split()))
    edges = []
    for i in range(N-1):
        edges.append(list(map(int, input().split())))
    ops = []
    for i in range(Q):
        ops.append(list(map(int, input().split())))
    #print(edges)
    #print(ops)
    #build tree
    tree = {}
    for i in range(N):
        tree[i+1] = []
    for e in edges:
        tree[e[0]].append(e[1])
        tree[e[1]].append(e[0])
    #print(tree)
    #dfs
    visited = [False] * (N+1)
    stack = [1]
    visited[1] = True
    order = []
    while len(stack) > 0:
        v = stack.pop()
        order.append(v)
        for c in tree[v]:
            if not visited[c]:
                visited[c] = True
                stack.append(c)
    #print(order)
    #calculate range of subtree
    ranges = {}
    for i in range(N):
        ranges[order[i]] = [i, i]
    for i in range(N-1, -1, -1):
        v = order[i]
        for c in tree[v]:
            if ranges[v][0] > ranges[c][0]:
                ranges[v][0] = ranges[c][0]
            if ranges[v][1] < ranges[c][1]:
                ranges[v][1] = ranges[c][1]
    #print(ranges)
    #calculate result
    result = [0] * N
    for op in ops:
        p = op[0]
        x = op[1]
        result[ranges[p][0]] += x
        if ranges[p][1] < N-1:
            result[ranges[p][1]+1] -= x
    #print(result)
    #print result
    for i in range(1, N):
        result[i] += result[i-1]
    print(' '.join(list(map(str, result))))
