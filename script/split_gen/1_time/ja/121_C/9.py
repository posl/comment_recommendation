def main():
    N, M = map(int, input().split())
    # A_i と B_i を格納するリスト
    A = []
    B = []
    # 入力を受け取る
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # A_i と B_i を一つのリストにまとめる
    AB = [[a, b] for a, b in zip(A, B)]
    # A_i でソートする
    AB.sort()
    # 購入する栄養ドリンクの本数
    drink = 0
    # 購入する栄養ドリンクの合計金額
    total = 0
    # 栄養ドリンクを M 本買うまでループする
    while drink < M:
        # A_i が最小の栄養ドリンクを買う
        total += AB[0][0] * AB[0][1]
        drink += AB[0][1]
        # 買った栄養ドリンクの本数を引く
        AB[0][1] = 0
        # A_i が最小の栄養ドリンクを買い切ったら、次の栄養ドリンクを買う
        if AB[0][1] == 0:
            AB.pop(0)
    # M 本買った後に、余った栄養ドリンクを買う
    total -= AB[0][0] * (drink - M)
    print(total)
