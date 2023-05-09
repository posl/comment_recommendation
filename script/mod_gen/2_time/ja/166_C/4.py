def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
    # 隣接リスト
    G = [[] for _ in range(N)]
    for i in range(M):
        G[A[i]].append(B[i])
        G[B[i]].append(A[i])
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

if __name__ == '__main__':
    main()