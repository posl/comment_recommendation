def main():
    N = int(input())
    node = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        node[u-1].append([v-1,w])
        node[v-1].append([u-1,w])
    ans = [-1]*N
    ans[0] = 0
    stack = [0]
    while stack:
        now = stack.pop()
        for next in node[now]:
            if ans[next[0]] == -1:
                ans[next[0]] = (ans[now] + next[1])%2
                stack.append(next[0])
    print(*ans,sep='
')

if __name__ == '__main__':
    main()