def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A.sort()
    # 0 から M-1 までの整数について、それぞれの整数が A に含まれるかどうかを記録するリスト
    # 0 から M-1 までの整数のうち、A に含まれる整数の個数を記録するリスト
    is_exist = [False] * M
    cnt = [0] * M
    for a in A:
        is_exist[a] = True
        cnt[a] += 1
    # A に含まれる整数のうち、最小の整数を求める
    min_a = 0
    while not is_exist[min_a]:
        min_a += 1
    # A に含まれる整数のうち、最大の整数を求める
    max_a = M - 1
    while not is_exist[max_a]:
        max_a -= 1
    # A に含まれる整数のうち、最大の整数から最小の整数までの距離を求める
    dist = max_a - min_a
    # 0 から M-1 までの整数について、それぞれの整数が A に含まれるかどうかを記録するリスト
    # 0 から M-1 までの整数のうち、A に含まれる整数の個数を記録するリスト
    # A に含まれる整数のうち、最小の整数
    # A に含まれる整数のうち、最大の整数
    # A に含まれる整数のうち、最大の整数から最小の整数までの距離
    # という情報を持つタプルを返す
    return is_exist, cnt,

if __name__ == '__main__':
    main()