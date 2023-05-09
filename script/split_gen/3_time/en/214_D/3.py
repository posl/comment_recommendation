def main():
    N = int(input())
    E = [[] for i in range(N)]
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        E[u].append((v, w))
        E[v].append((u, w))
    #print(E)
    #print()
    # 1. DFS to find the maximum edge in each subtree
    # 2. DFS to find the maximum edge in each path
    # 1. DFS to find the maximum edge in each subtree
    # 1.1. Initialize
    T = [0] * N
    for i in range(N):
        T[i] = [0, 0]
    # 1.2. DFS
    stack = [0]
    while stack:
        i = stack.pop()
        for j, w in E[i]:
            if T[j][0] == 0:
                T[j][0] = w
                T[j][1] = i
                stack.append(j)
    #print(T)
    #print()
    # 2. DFS to find the maximum edge in each path
    # 2.1. Initialize
    P = [0] * N
    for i in range(N):
        P[i] = [0, 0]
    # 2.2. DFS
    stack = [0]
    while stack:
        i = stack.pop()
        for j, w in E[i]:
            if P[j][0] == 0:
                P[j][0] = max(w, T[i][0])
                P[j][1] = i
                stack.append(j)
    #print(P)
    #print()
    # 3. Calculate the answer
    ans = 0
    for i in range(N):
        ans += P[i][0]
    print(ans)
