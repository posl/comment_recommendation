def main():
    N,X,Y = map(int,input().split())
    U = [0]*(N-1)
    V = [0]*(N-1)
    for i in range(N-1):
        U[i],V[i] = map(int,input().split())
    #print(N,X,Y)
    #print(U,V)
    #print("-----")
    
    #树形结构
    tree = [[] for i in range(N+1)]
    for i in range(N-1):
        tree[U[i]].append(V[i])
        tree[V[i]].append(U[i])
    #print(tree)
    
    #深度优先搜索
    #print("深度优先搜索")
    #print("-----")
    #print("从顶点X到顶点Y的简单路径上的所有顶点的索引")
    #print("中间有空格")
    #print("-----")
    ans = []
    def dfs(now,pre):
        if now == Y:
            ans.append(now)
            return True
        for next in tree[now]:
            if next == pre:
                continue
            if dfs(next,now):
                ans.append(now)
                return True
        return False
    dfs(X,-1)
    ans = ans[::-1]
    print(" ".join(map(str,ans)))

if __name__ == '__main__':
    main()