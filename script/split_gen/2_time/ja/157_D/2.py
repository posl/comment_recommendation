def main():
    N, M, K = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * K
    D = [0] * K
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    #友達関係をリスト化
    friend = [[] for _ in range(N+1)]
    for i in range(M):
        friend[A[i]].append(B[i])
        friend[B[i]].append(A[i])
    #ブロック関係をリスト化
    block = [[] for _ in range(N+1)]
    for i in range(K):
        block[C[i]].append(D[i])
        block[D[i]].append(C[i])
    #人iの友達候補数を求める
    ans = [0] * (N+1)
    for i in range(1, N+1):
        ans[i] = N - len(friend[i]) - 1
        for j in friend[i]:
            if i in block[j]:
                ans[i] -= 1
    for i in range(1, N+1):
        print(ans[i], end=" ")
