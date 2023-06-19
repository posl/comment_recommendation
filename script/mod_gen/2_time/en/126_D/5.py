def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    
    N = int(input())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        E[u-1].append((v-1,w))
        E[v-1].append((u-1,w))
    
    ans = [-1]*N
    ans[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for nv,nw in E[v]:
            if ans[nv] == -1:
                ans[nv] = ans[v] + nw
                que.append(nv)
    
    for a in ans:
        print(a%2)
main()
