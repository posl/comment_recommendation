Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1

    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1

    print(x4, y4)

=======
Suggestion 2

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    elif x2 == x3:
        x4 = x1
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    elif y2 == y3:
        y4 = y1
    print(x4, y4)

=======
Suggestion 3

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if x1 == x2:
        x = x3
    elif x1 == x3:
        x = x2
    else:
        x = x1
    if y1 == y2:
        y = y3
    elif y1 == y3:
        y = y2
    else:
        y = y1
    print(x, y)

=======
Suggestion 4

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if x1 != x2 and x1 != x3:
        x = x1
    elif x2 != x1 and x2 != x3:
        x = x2
    else:
        x = x3
    if y1 != y2 and y1 != y3:
        y = y1
    elif y2 != y1 and y2 != y3:
        y = y2
    else:
        y = y3
    print(x, y)

=======
Suggestion 5

def main():
    #入力
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    #出力
    if (x1 == x2):
        print(x3, end = " ")
    elif (x1 == x3):
        print(x2, end = " ")
    else:
        print(x1, end = " ")
    if (y1 == y2):
        print(y3, end = " ")
    elif (y1 == y3):
        print(y2, end = " ")
    else:
        print(y1, end = " ")

main()

=======
Suggestion 6

def main():
    #入力
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    
    #出力
    if x1 == x2:
        print(x3, end=" ")
    elif x1 == x3:
        print(x2, end=" ")
    else:
        print(x1, end=" ")
    if y1 == y2:
        print(y3)
    elif y1 == y3:
        print(y2)
    else:
        print(y1)

=======
Suggestion 7

def main():
    x = []
    y = []
    for i in range(3):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(3):
        if x.count(x[i]) == 1:
            x = x[i]
            break
    for i in range(3):
        if y.count(y[i]) == 1:
            y = y[i]
            break
    print(x, y)

=======
Suggestion 8

def main():
    # 3つの座標を取得
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))

    # 座標のリストを作成
    c_list = [c1, c2, c3]
    #print(c_list)

    # x座標のリストを作成
    x_list = []
    # y座標のリストを作成
    y_list = []

    # 座標のリストからx座標とy座標のリストを作成
    for i in range(3):
        x_list.append(c_list[i][0])
        y_list.append(c_list[i][1])

    #print(x_list)
    #print(y_list)

    # x座標とy座標のリストから重複する値を削除
    x_list = list(set(x_list))
    y_list = list(set(y_list))

    #print(x_list)
    #print(y_list)

    # x座標のリストから重複する値を削除した後のリストの要素数が2の場合
    if len(x_list) == 2:
        # x座標のリストの要素数が2の場合
        # y座標のリストから重複する値を削除した後のリストの要素数が1の場合
        if len(y_list) == 1:
            # x座標のリストから重複する値を削除した後のリストの要素数が2の場合
            # y座標のリストの要素数が1の場合
            # x座標のリストの要素数が2の場合
            # 重複する値を削除した後のリストの要素数が1の場合
            # x座標のリストから重
