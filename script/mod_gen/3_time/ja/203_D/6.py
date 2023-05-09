def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # 中央値を求める
    def get_median(A):
        A.sort()
        return A[len(A) // 2]
    # 区画の中央値を求める
    def get_median_area(A, x, y, k):
        tmp = []
        for i in range(k):
            for j in range(k):
                tmp.append(A[x + i][y + j])
        return get_median(tmp)
    # 区画の中央値の最小値を求める
    ans = 10**9
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            ans = min(ans, get_median_area(A, i, j, K))
    print(ans)

if __name__ == '__main__':
    main()