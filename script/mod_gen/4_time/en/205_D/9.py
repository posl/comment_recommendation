def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # 1. A_iとA_{i+1}の差が1以上あることを確認
    for i in range(N-1):
        if A[i+1] - A[i] <= 1:
            print("A_iとA_{i+1}の差が1以上でない")
            return
    # 2. A_iが1以上であることを確認
    if A[0] != 1:
        print("A_iが1でない")
        return
    # 3. A_iが1以上であることを確認
    if A[N-1] >= 10**18:
        print("A_iが10^18以上である")
        return
    # 4. K_iが1以上であることを確認
    for i in range(Q):
        if K[i] < 1:
            print("K_iが1未満である")
            return
    # 5. K_iが10^18以下であることを確認
    if max(K) >= 10**18:
        print("K_iが10^18以上である")
        return
    # 6. 上記の条件を満たすならば、1, 2, 4, 8, 9, 10, 11, ... という数列からK_i番目の数を出力
    # 7. 1, 2, 4, 8, 9, 10, 11, ... という数列のi番目の数は、A_i-1番目の数に2^iを足したものである
    for i in range(Q):
        for j in range(N-1):
            if K[i] <= A[j+1] - A[j] - 1:
                print(A[j] + K[i])
                break
            else:
                K[i] -= A[j+1] - A[j] -

if __name__ == '__main__':
    main()