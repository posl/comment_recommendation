def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 一番遠い家と一番近い家の距離を求める
    max_dist = 0
    for i in range(N - 1):
        dist = A[i + 1] - A[i]
        max_dist = max(max_dist, dist)
    # 一番遠い家と一番近い家の距離のうち、一周した場合の距離を考慮する
    dist = K - A[-1] + A[0]
    max_dist = max(max_dist, dist)
    # 一番遠い家と一番近い家の距離のうち、一番遠い家から一番近い家に向かう距離を求める
    print(K - max_dist)

if __name__ == '__main__':
    main()