def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    
    N,Q = map(int,input().split())
    edge = [[] for i in range(N+1)]
    for i in range(N-1):
        a,b = map(int,input().split())
        edge[a].append(b)
        edge[b].append(a)
    
    depth = [-1]*(N+1)
    depth[1] = 0
    que = deque([1])
    while que:
        p = que.popleft()
        for i in edge[p]:
            if depth[i] == -1:
                depth[i] = depth[p]+1
                que.append(i)
    
    for i in range(Q):
        c,d = map(int,input().split())
        if abs(depth[c]-depth[d])%2 == 0:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()