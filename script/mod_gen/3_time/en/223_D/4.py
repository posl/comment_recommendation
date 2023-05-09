def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
    ans = [-1]*N
    for i in range(N):
        if ans[i] == -1:
            ans[i] = i+1
            for j in G[i]:
                if ans[j] == -1:
                    ans[j] = i+1
                else:
                    print(-1)
                    return
    print(*ans)

if __name__ == '__main__':
    main()