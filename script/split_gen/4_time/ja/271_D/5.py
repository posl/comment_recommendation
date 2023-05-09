def main():
    # 入力
    n, s = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]
    # 組み合わせを全探索
    for i in range(2**n):
        # 2進数で表す
        bit = format(i, 'b').zfill(n)
        # 表の合計値
        sum_t = 0
        # 裏の合計値
        sum_f = 0
        for j in range(n):
            # 1なら表
            if bit[j] == '1':
                sum_t += cards[j][0]
            # 0なら裏
            else:
                sum_f += cards[j][1]
        # 表の合計値と裏の合計値が等しければ終了
        if sum_t == s == sum_f:
            print('Yes')
            print(bit.replace('1', 'H').replace('0', 'T'))
            return
    # 組み合わせがなければNo
    print('No')
