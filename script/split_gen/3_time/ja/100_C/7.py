def main():
    # 入力
    N = int(input())
    a = [int(x) for x in input().split()]
    # 処理
    count = 0
    while True:
        if all([x % 2 == 0 for x in a]):
            a = [x // 2 for x in a]
            count += 1
        else:
            break
    # 出力
    print(count)
