def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    block = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)
    for _ in range(K):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        block[c].append(d)
        block[d].append(c)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friends[i]) - 1
    visited = [False] * N
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        q = [i]
        while q:
            x = q.pop()
            for y in friends[x]:
                if visited[y]:
                    continue
                visited[y] = True
                q.append(y)
                ans[i] -= 1
                ans[y] -= 1
                for z in block[y]:
                    if visited[z]:
                        continue
                    ans[z] -= 1
    print(*ans)
main()

if __name__ == '__main__':
    main()