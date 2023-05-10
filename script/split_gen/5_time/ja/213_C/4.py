def main():
    # 標準入力受付
    h, w, n = map(int, input().split())
    cards = []
    for i in range(n):
        a, b = map(int, input().split())
        cards.append((a, b, i + 1))
    # 行の削除
    cards.sort(key=lambda x: x[0])
    row = 1
    for i in range(n):
        if row != cards[i][0]:
            row = cards[i][0]
        cards[i] = (row, cards[i][1], cards[i][2])
    # 列の削除
    cards.sort(key=lambda x: x[1])
    col = 1
    for i in range(n):
        if col != cards[i][1]:
            col = cards[i][1]
        cards[i] = (cards[i][0], col, cards[i][2])
    # 答えの出力
    cards.sort(key=lambda x: x[2])
    for i in range(n):
        print(cards[i][0], cards[i][1])
