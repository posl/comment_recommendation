def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    # 全順列を作る
    from itertools import permutations
    all_perm = permutations(range(N))
    # 距離を計算する関数
    def calc_dist(a, b):
        return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    # 全順列を走査して、距離の合計を計算する
    sum_dist = 0
    for perm in all_perm:
        for i in range(N-1):
            sum_dist += calc_dist(XY[perm[i]], XY[perm[i+1]])
    # 距離の合計を全順列数で割る
    print(sum_dist/len(list(all_perm)))

if __name__ == '__main__':
    main()