def main():
    L,Q = map(int,input().split())
    tree = [0,L]
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            tree.append(x)
        else:
            tree.sort()
            left = tree.index(x)
            print(tree[left]-tree[left-1])
