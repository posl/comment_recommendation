def count_operation(a, x):
    # aに対してxを作るために必要な操作回数を返す
    # xがaより大きい場合はマイナスの操作が必要
    # xがaより小さい場合はプラスの操作が必要
    # xがaと等しい場合は操作不要
    return abs(x - a)

if __name__ == '__main__':
    count_operation()