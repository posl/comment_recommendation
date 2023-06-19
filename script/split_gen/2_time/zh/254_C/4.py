def solve(N, K, A):
    # Kを大きい順にソートする
    K.sort(reverse=True)
    # Kの最大値がAの長さの半分以上の場合、必ずNo
    if K[0] >= N // 2:
        return 'No'
    # Kの最大値がAの最大値以下の場合、必ずYes
    if K[0] >= max(A):
        return 'Yes'
    # Kの最大値がAの最大値より大きい場合、可能性があるか調べる
    for i in range(len(K)):
        # Kの値がAの最大値以下であれば、可能性がある
        if K[i] <= max(A):
            return 'Yes'
        # Kの値がAの最大値より大きければ、Kの値を減らして再チャレンジ
        else:
            K[i] -= 1
    # 結局、可能性がない場合はNo
    return 'No'
