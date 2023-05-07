def main():
    N, Q = map(int, input().split())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    p = []
    x = []
    for i in range(Q):
        p_i, x_i = map(int, input().split())
        p.append(p_i)
        x.append(x_i)
    #print(N, Q)
    #print(a)
    #print(b)
    #print(p)
    #print(x)
    #print("")
    # initialize the tree
    tree = {}
    for i in range(N):
        tree[i+1] = []
    # link the tree
    for i in range(N-1):
        tree[a[i]].append(b[i])
        tree[b[i]].append(a[i])
    #print(tree)
    # initialize the counter
    counter = [0 for i in range(N)]
    #print(counter)
    # operation
    for i in range(Q):
        counter[p[i]-1] += x[i]
    #print(counter)
    # dfs
    stack = [1]
    visited = []
    while stack:
        v = stack.pop()
        visited.append(v)
        for child in tree[v]:
            if child not in visited:
                stack.append(child)
                counter[child-1] += counter[v-1]
    #print(counter)
    # output
    for i in range(N):
        print(counter[i], end=" ")
    print("")

if __name__ == '__main__':
    main()