def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    
    add = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        add[p - 1] += x
    
    ans = [0] * N
    que = [0]
    while que:
        now = que.pop()
        for nxt in edge[now]:
            if ans[nxt] == 0:
                ans[nxt] = ans[now] + add[nxt]
                que.append(nxt)
    
    for i in range(N):
        if ans[i] == 0:
            ans[i] = add[i]
    
    print(*ans)

if __name__ == '__main__':
    main()