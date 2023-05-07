def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # 6連続の黒マスが存在するか判定する
    def is_6consecutive_black():
        for i in range(N-5):
            for j in range(N-5):
                # 6行6列のマス目を取得
                S_ = [S[k][j:j+6] for k in range(i, i+6)]
                # 一つでも黒マスがなければNG
                if '#' not in ''.join(S_):
                    continue
                # 対角線上のマスがすべて黒マスであればOK
                if all(S_[k][k] == '#' for k in range(6)):
                    return True
        return False
    # 白マスの数を数える
    cnt = sum(s.count('.') for s in S)
    if cnt == 0:
        # 白マスがなければOK
        print('Yes')
    elif cnt == 1:
        # 白マスが1つならば、そのマスを黒く塗ればOK
        print('Yes')
    else:
        # 白マスが2つ以上あれば、2つのマスを黒く塗ればOK
        print('Yes' if is_6consecutive_black() else 'No')
main()

if __name__ == '__main__':
    main()