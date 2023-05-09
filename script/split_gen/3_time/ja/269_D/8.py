def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    #各マスの座標を格納する
    XY = set(map(tuple, XY))
    #連結成分の数
    ans = 0
    #XYに要素が残っている限り
    while XY:
        #XYの中から一つ取り出す
        x, y = XY.pop()
        #取り出したマスをスタックに入れる
        stack = [(x, y)]
        #スタックが空になるまで
        while stack:
            #スタックから1つ取り出す
            x, y = stack.pop()
            #取り出したマスの隣接するマスを調べる
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1)]:
                #隣接するマスがXYに含まれているか
                if (x + dx, y + dy) in XY:
                    #含まれていればスタックに入れる
                    stack.append((x + dx, y + dy))
                    #XYから取り出したマスを消す
                    XY.remove((x + dx, y + dy))
        #スタックが空になったら連結成分が1つ見つかった
        ans += 1
    print(ans)
