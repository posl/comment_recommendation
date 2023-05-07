def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # まずは素因数分解して素因数のリストを作成
    A_factor = []
    for i in range(N):
        A_factor.append([])
        temp = A[i]
        for j in range(2, int(A[i]**(1/2))+1):
            while temp % j == 0:
                A_factor[i].append(j)
                temp //= j
        if temp != 1:
            A_factor[i].append(temp)
    # 素因数のリストを繋げる
    A_factor_all = []
    for i in range(N):
        A_factor_all += A_factor[i]
    # 素因数のリストから重複を削除
    A_factor_all = list(set(A_factor_all))
    # 素因数のリストから半公倍数を作成
    half_multiple = []
    for i in range(len(A_factor_all)):
        temp = A_factor_all[i]
        while temp <= M:
            half_multiple.append(temp)
            temp *= 2
    # 半公倍数のリストから重複を削除
    half_multiple = list(set(half_multiple))
    # 半公倍数のリストからAの要素の倍数を削除
    for i in range(N):
        for j in range(len(half_multiple)):
            if half_multiple[j] % A[i] == 0:
                half_multiple[j] = 0
    half_multiple = list(set(half_multiple))
    half_multiple.remove(0)
    # 半公倍数の個数を出力
    print(len(half_multiple))
