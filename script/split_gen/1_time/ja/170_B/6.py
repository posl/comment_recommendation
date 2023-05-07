def main():
    #入力
    X, Y = map(int, input().split())
    #処理
    if (Y % 2 == 0) and (Y // 2 >= X) and (Y // 2 <= 2 * X):
        print('Yes')
    else:
        print('No')
