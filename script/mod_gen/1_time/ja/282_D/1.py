def main():
    N, M = map(int, input().split())
    edge = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if j in edge[i]:
                continue
            else:
                if len(edge[i]) + len(edge[j]) == N-2:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()