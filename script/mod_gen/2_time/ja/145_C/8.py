def main():
    N = int(input())
    x_y = [list(map(int, input().split())) for _ in range(N)]
    # 順列を作成
    import itertools
    perm = itertools.permutations(range(N))
    # 距離を計算
    import math
    distance = 0
    for p in perm:
        for i in range(N-1):
            distance += math.sqrt((x_y[p[i]][0]-x_y[p[i+1]][0])**2 + (x_y[p[i]][1]-x_y[p[i+1]][1])**2)
    # 平均値を出力
    print(distance/(math.factorial(N)))

if __name__ == '__main__':
    main()