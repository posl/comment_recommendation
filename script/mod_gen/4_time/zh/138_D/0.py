def cal_tree():
    n,q = map(int,input().split())
    tree = {}
    for i in range(n-1):
        a,b = map(int,input().split())
        if a in tree:
            tree[a].append(b)
        else:
            tree[a] = [b]
    #print(tree)
    #print(tree[1][

if __name__ == '__main__':
    cal_tree()