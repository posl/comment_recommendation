def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = []
    for i in range(Q):
        K.append(int(input()))
    #print(N, Q, A, K)
    # Aの最大値を求める
    max_A = max(A)
    # Aの最大値より大きい値を求める
    max_A_plus = 0
    for i in range(N):
        if max_A < A[i]:
            max_A_plus = A[i]
            break
    # Aの最大値より大きい値のindexを求める
    max_A_plus_index = 0
    for i in range(N):
        if max_A < A[i]:
            max_A_plus_index = i
            break
    # Aの最大値より大きい値を含めたリストを作成する
    A_plus = A[:max_A_plus_index] + [max_A_plus] + A[max_A_plus_index:]
    # Aの最大値より大きい値を含めたリストの累積和を求める
    A_plus_cumsum = [0]
    for i in range(len(A_plus)):
        A_plus_cumsum.append(A_plus_cumsum[i] + A_plus[i])
    #print(A_plus, A_plus_cumsum)
    # Kの値を使って、Aの最大値より大きい値を含めたリストの累積和の値を求める
    for i in range(Q):
        # Kの値がAの最大値より大きい場合
        if K[i] > max_A:
            # Aの最大値より大きい値のindexを求める
            max_A_plus_index = 0
            for j in range(N):
                if max_A < A[j]:
                    max_A_plus_index = j
                    break
            #print(max_A_plus_index)
            #print(A_plus_cumsum)
            print(A_plus_cumsum[max_A_plus_index] + (K[i] - max_A) * (N - max_A_plus_index))
        # Kの値

if __name__ == '__main__':
    main()