def main():
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    # 1. 操作回数の最小値を求める
    # 2. 操作回数の最小値が奇数の場合、操作回数の最小値 + 1 を求める
    # 3. 操作回数の最小値が偶数の場合、操作回数の最小値を求める
    # 4. 1, 2, 3 を繰り返す
    # 1. 操作回数の最小値を求める
    # 2. 操作回数の最小値が奇数の場合、操作回数の最小値 + 1 を求める
    # 3. 操作回数の最小値が偶数の場合、操作回数の最小値を求める
    # 4. 1, 2, 3 を繰り返す
    # 1. 操作回数の最小値を求める
    # 2. 操作回数の最小値が奇数の場合、操作回数の最小値 + 1 を求める
    # 3. 操作回数の最小値が偶数の場合、操作回数の最小値を求める
    # 4. 1, 2, 3 を繰り返す
    # 1. 操作回数の最小値を求める
    # 2. 操作回数の最小値が奇数の場合、操作回数の最小値 + 1 を求める
    # 3. 操作回数の最小

if __name__ == '__main__':
    main()