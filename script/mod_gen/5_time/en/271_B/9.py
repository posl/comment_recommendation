def main():
    N, Q = map(int, input().split())
    # 2次元配列を作成
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    # クエリを処理
    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

if __name__ == '__main__':
    main()