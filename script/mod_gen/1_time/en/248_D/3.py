def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    Q = int(input())
    query = []
    for _ in range(Q):
        L, R, X = [int(a) for a in input().split()]
        query.append((L, R, X))
    # 1. 1-indexedにする
    # 2. 1-indexedにしたAを、A[i]を値とする要素の数を数える
    A = [0] + A
    count = [0] * (N + 1)
    for a in A:
        count[a] += 1
    # 3. 累積和を取る
    cumsum = [0] * (N + 1)
    for i in range(1, N + 1):
        cumsum[i] = cumsum[i - 1] + count[i]
    # 4. 累積和を用いて、各クエリに対する解を出力する
    for L, R, X in query:
        print(cumsum[R] - cumsum[L - 1])

if __name__ == '__main__':
    main()