def permutations(arr, n):
    # 順列を出力する
    # arr: 対象配列
    # n: 順列の長さ
    # 戻り値: 順列のリスト
    if n == 0:
        return [[]]
    l = []
    for i in range(len(arr)):
        m = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest, n - 1):
            l.append([m] + p)
    return l

if __name__ == '__main__':
    permutations()