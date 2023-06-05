def main():
    N, M, K = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for _ in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    # print(N, M, K)
    # print(A)
    # print(B)
    # print(C)
    # print(D)
    # 建立图
    graph = {}
    for i in range(M):
        if A[i] not in graph:
            graph[A[i]] = [B[i]]
        else:
            graph[A[i]].append(B[i])
        if B[i] not in graph:
            graph[B[i]] = [A[i]]
        else:
            graph[B[i]].append(A[i])
    # print(graph)
    # 计算每个节点的候选好友
    ans = [0] * N
    for i in range(1, N + 1):
        if i in graph:
            for j in graph[i]:
                if j not in graph:
                    continue
                for k in graph[j]:
                    if k not in graph:
                        continue
                    if k != i and k not in graph[i]:
                        ans[i - 1] += 1
    print(' '.join(map(str, ans)))
