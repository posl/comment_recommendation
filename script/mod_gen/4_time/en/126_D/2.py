def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))
    ans = [0]*N
    stack = [(0,0)]
    while stack:
        p,c = stack.pop()
        ans[p] = c
        for q,d in G[p]:
            if ans[q] == -1:
                stack.append((q,c^d%2))
    print('
'.join(map(str,ans)))

if __name__ == '__main__':
    main()