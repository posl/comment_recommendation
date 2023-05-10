def main():
    # 標準入力から値を取得する
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = input().split()
        t = int(t)
        mountains.append([s, t])
    # 高さでソートする
    mountains.sort(key=lambda x: x[1], reverse=True)
    # 2番目に高い山の名前を出力
    print(mountains[1][0])

if __name__ == '__main__':
    main()