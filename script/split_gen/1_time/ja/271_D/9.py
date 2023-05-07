def main():
    # 入力
    N,S = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    # 1枚目の選択
    for i in range(2**N):
        # 2進数に変換
        i = bin(i)[2:].zfill(N)
        # 各カードの表と裏の和を計算
        sum_a = 0
        sum_b = 0
        for j in range(N):
            if i[j] == '0':
                sum_a += a[j]
            else:
                sum_b += b[j]
        # 和がSと一致する場合
        if sum_a + sum_b == S:
            print('Yes')
            print(i)
            return
    print('No')
    return
