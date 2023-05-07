def main():
    N, M = map(int, input().split())
    friends = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].add(b)
        friends[b].add(a)
    #print(friends)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        q = [i]
        while q:
            v = q.pop()
            if visited[v]:
                continue
            visited[v] = True
            for u in friends[v]:
                q.append(u)
    print(ans)
