def main():
    n,x,y=map(int,input().split())
    x,y=x-1,y-1
    tree=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    #print(tree)
    #print(x,y)
    #print(tree[x])
    #print(tree[y])
    #print(set(tree[x])&set(tree[y]))
    #print(set(tree[x])|set(tree[y]))
    #print(set(tree[x])^set(tree[y]))
    #print(set(tree[x])^set(tree[y])&set(tree[x]))
    #print(set(tree[x])^set(tree[y])&set(tree[y]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y])&set(tree[x]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y])&set(tree[y]))
    #print(set(tree[x])^set(tree[y])&set(tree[y])|set(tree[x])^set(tree[y])&set(tree[x])|set(tree[x])^set(tree[y])&set(tree[x])|set
