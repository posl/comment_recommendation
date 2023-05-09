def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # print(N, X)
    # print(A)
    # 素因数分解の結果を格納するリスト
    factorization = []
    # 素因数分解
    for i in range(N):
        # print(A[i])
        for j in range(1, A[i][0]+1):
            # print(A[i][j])
            # 素因数分解
            for k in range(2, A[i][j]):
                while A[i][j] % k == 0:
                    A[i][j] = A[i][j] // k
                    # print(A[i][j])
                    factorization.append(k)
    # print(factorization)
    # 素因数分解の結果を集計
    factorization_count = {}
    for i in range(len(factorization)):
        if factorization[i] in factorization_count:
            factorization_count[factorization[i]] += 1
        else:
            factorization_count[factorization[i]] = 1
    # print(factorization_count)
    # 素因数分解の結果を集計
    factorization_count_list = []
    for key, value in factorization_count.items():
        factorization_count_list.append(value)
    # print(factorization_count_list)
    # 素因数分解の結果を集計
    factorization_count_list.sort()
    # print(factorization_count_list)
    # 約数の個数の最大値
    max_divisor_count = 1
    for i in range(len(factorization_count_list)):
        max_divisor_count = max_divisor_count * (factorization_count_list[i] + 1)
    # print(max_divisor_count)
    # 約数の個数の最小値
    min_divisor_count = 1
    for i in range(len(factorization_count_list)):
        min_divisor_count = min_divisor_count * (factorization_count_list[i] + 1)
    # print(min_divisor_count)
    # 約数の個数の最小値
    min_div

if __name__ == '__main__':
    main()