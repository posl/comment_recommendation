def main():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        E[a-1].append(b-1)
        E[b-1].append(a-1)
    #print(E)
    visited = [0]*N
    group = 0
    for i in range(N):
        if visited[i] == 0:
            group += 1
            visited[i] = group
            stack = [i]
            while stack:
                v = stack.pop()
                for w in E[v]:
                    if visited[w] == 0:
                        visited[w] = group
                        stack.append(w)
    print(group)
