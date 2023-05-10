def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # 一番上にあるカードの番号を保持
    top_card_num = p[0]
    # 一番上にあるカードの番号のカードが何枚目に食べられるかを保持
    top_card_num_eaten = 1
    # 一番上にあるカードの番号のカードが何枚目に置かれたかを保持
    top_card_num_put = 1
    # 一番上にあるカードの番号のカードが何枚目に重ねられたかを保持
    top_card_num_stack = 1
    # 一番上にあるカードの番号のカードが何枚目に食べられるかを計算
    for i in range(1, n):
        if p[i] > top_card_num:
            top_card_num_eaten += 1
        else:
            top_card_num_put = i + 1
            top_card_num_stack = i + 1
            break
    # 一番上にあるカードの番号のカードが何枚目に重ねられたかを計算
    for i in range(top_card_num_put, n):
        if p[i] > top_card_num:
            top_card_num_stack += 1
        else:
            break
    # 一番上にあるカードの番号のカードが何枚目に食べられるかを出力
    print(top_card_num_eaten)
    # 一番上にあるカードの番号のカードが何枚目に重ねられたかを計算
    for i in range(2, n + 1):
        # カードが食べられる場合
        if i - top_card_num_eaten == k:
            # 一番上にあるカードの番号を更新
            top_card_num = p[i - 1]
            # 一番上にある

if __name__ == '__main__':
    main()