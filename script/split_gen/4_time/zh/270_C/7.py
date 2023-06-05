def main():
    n,x,y = map(int,input().split())
    tree = []
    for i in range(n-1):
        u,v = map(int,input().split())
        tree.append((u,v))
    #print(tree)
    path = []
    path.append(x)
    while True:
        for i in range(len(tree)):
            if tree[i][0] == x:
                x = tree[i][1]
                path.append(x)
                break
            if tree[i][1] == x:
                x = tree[i][0]
                path.append(x)
                break
        if x == y:
            break
    print(*path)
