def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [None] * M
    B = [None] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M, H, A, B)
    G = [[] for _ in range(N)]
    for a, b in zip(A, B):
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    #print(G)
    ans = 0
    for i in range(N):
        flag = True
        for j in G[i]:
            if H[i] <= H[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
