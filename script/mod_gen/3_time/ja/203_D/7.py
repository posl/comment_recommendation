def main():
    #入力
    N, K = map(int, input().split())
    A = [[int(i) for i in input().split()] for j in range(N)]
    #K×Kの区画の中央値の最小値を求める
    ans = 10 ** 9 + 1
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            #区画の中央値を求める
            tmp = []
            for k in range(K):
                for l in range(K):
                    tmp.append(A[i + k][j + l])
            tmp.sort()
            ans = min(ans, tmp[(K ** 2) // 2])
    #出力
    print(ans)

if __name__ == '__main__':
    main()