def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    graph = [[] for i in range(N+1)]
    for i in range(M):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])
    ans = [0] * (N+1)
    ans[1] = -1
    que = [1]
    while que:
        now = que.pop()
        for i in graph[now]:
            if ans[i] == 0:
                ans[i] = now
                que.append(i)
    if 0 in ans[2:]:
        print("No")
    else:
        print("Yes")
        for i in range(2, N+1):
            print(ans[i])
