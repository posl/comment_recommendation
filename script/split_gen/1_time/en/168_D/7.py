def main():
    # taking input
    n, m = map(int, input().split())
    # making the graph
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    # making the tree
    tree = [0] * n
    tree[0] = -1
    q = [0]
    while q:
        node = q.pop()
        for child in graph[node]:
            if tree[child] == 0:
                tree[child] = node + 1
                q.append(child)
    # checking if the tree is valid
    for i in range(1, n):
        if tree[i] == 0:
            print('No')
            return
    # printing the tree
    print('Yes')
    for i in range(1, n):
        print(tree[i])
