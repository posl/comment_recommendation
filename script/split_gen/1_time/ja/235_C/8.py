def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0 for _ in range(Q)]
    K = [0 for _ in range(Q)]
    for i in range(Q):
        X[i], K[i] = map(int, input().split())
    # Aの要素をxに分類
    # Aの要素に対応するindexを格納
    # 例) x = 1の要素のindexはindex[1]
    index = [[] for _ in range(10**9+1)]
    for i in range(N):
        index[A[i]].append(i)
    
    # Xの要素に対応するindexを格納
    # 例) Xの要素x = 1のindexはindex[1]
    index2 = [[] for _ in range(10**9+1)]
    for i in range(Q):
        index2[X[i]].append(i)
    # Xの要素に対応するindexを格納
    # 例) Xの要素x = 1のindexはindex[1]
    ans = [-1 for _ in range(Q)]
    for i in range(10**9+1):
        if len(index[i]) == 0:
            continue
        for j in index2[i]:
            if K[j] <= len(index[i]):
                ans[j] = index[i][K[j]-1] + 1
    for i in range(Q):
        print(ans[i])
