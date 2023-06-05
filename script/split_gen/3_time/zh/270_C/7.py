def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    tree = {}
    for i in range(N-1):
        U, V = map(int, input().split())
        #print(U, V)
        if U not in tree:
            tree[U] = [V]
        else:
            tree[U].append(V)
        if V not in tree:
            tree[V] = [U]
        else:
            tree[V].append(U)
    #print(tree)
    path = [X]
    while path[-1] != Y:
        if len(tree[path[-1]]) == 1:
            path.pop()
        else:
            for i in range(len(tree[path[-1]])-1, -1, -1):
                if tree[path[-1]][i] == path[-2]:
                    tree[path[-1]].pop(i)
            path.append(tree[path[-1]][-1])
    print(*path)
