def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # 各カードの位置を記録
    card_pos = [0] * N
    for i in range(N):
        card_pos[P[i]-1] = i
    # 各カードが何回目に消えるかを記録
    card_eat = [-1] * N
    for i in range(N):
        # カードが消えていない場合
        if card_eat[i] == -1:
            # カードの位置を記録
            pos = card_pos[i]
            # 消えるカードの数を数える
            eat_cnt = 0
            while True:
                # カードが消えている場合
                if card_eat[P[pos]-1] != -1:
                    break
                # カードを消す
                card_eat[P[pos]-1] = i+1
                # 消えるカードの数を増やす
                eat_cnt += 1
                # カードの位置を進める
                pos += K
                # カードの位置が範囲外の場合
                if pos >= N:
                    pos -= N
            # 消えるカードの数を記録
            for j in range(eat_cnt):
                card_eat[P[pos]-1] = i+1
    # 結果を出力
    for i in range(N):
        print(card_eat[i])
