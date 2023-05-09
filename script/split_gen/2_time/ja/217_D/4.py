def main():
    L, Q = map(int, input().split())
    # 木材の長さを格納するリスト
    wood = [L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            # 線 x がある地点で木材を 2 つに切る
            tmp = []
            for w in wood:
                if w > x:
                    tmp.append(w - x)
                    tmp.append(x)
                    wood.remove(w)
                    break
            wood += tmp
        else:
            # 線 x を含む木材を選び、その長さを出力する
            for w in wood:
                if w >= x:
                    print(w)
                    break
